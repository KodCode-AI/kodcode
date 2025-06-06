import os
import sys
import argparse
import json
import re
import torch
import numpy as np
from tqdm import tqdm
from jinja2 import Environment, FileSystemLoader, exceptions
from sentence_transformers import SentenceTransformer
import faiss
from datasets import load_dataset

################
# Configurations
################
def get_args():
    parser = argparse.ArgumentParser(description="Instruction Extraction and Sanitization Manager.")
    
    # Input Parameters
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input JSONL file.")

    # Similarity Parameters
    parser.add_argument("--sentence_model", type=str, default="sentence-transformers/all-mpnet-base-v2", help="SentenceTransformer model for encoding instructions.")
    parser.add_argument("--encoding_batch_size", type=int, default=256, help="Batch size for encoding sentences.")
    parser.add_argument("--distance_threshold", type=float, default=0.1, help="Cosine similarity threshold for filtering similar instructions.")
    parser.add_argument("--search_space_size", type=int, default=100, help="Number of nearest neighbors to search for similarity.")
    parser.add_argument("--search_batch_size", type=int, default=4096, help="Batch size for searching similarity.")

    # Device Configuration
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu", help="Device to run the model on ('cuda' or 'cpu').")

    return parser.parse_args()

def get_prompt(instruction):
    """
    Loads and renders the prompt template with the given instruction.
    """
    env = Environment(loader=FileSystemLoader('prompts'))
    template = env.get_template('gen_responses.md').render()
    return template + instruction

def extract_instruction(message_content):
    """
    Extracts the instruction from the assistant's message content.
    Removes any leading "Question X" or similar prefixes.
    """
    instruction = message_content.strip()
    
    # Remove leading "Question X" where X is a number (e.g., "Question 4:", "### Question 4:", etc.)
    # Remove various forms of "Question" prefixes
    instruction = re.sub(r'^\[?Question\s*\d*\]?:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^#+\s*\[?Question\s*\d*\]?:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\[?Question\s*\d*\]?:.*?$', '', instruction, flags=re.IGNORECASE | re.MULTILINE)
    instruction = re.sub(r'^#+\s*New\s+Question:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\*\*Question\s*\d*:?\*\*\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\*\*Question:?\*\*\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\[?Question\s*\d+\]?:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^#+\s*\[?Question\s*\d+\]?:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\[?Question\s*\d+\]?:.*?$', '', instruction, flags=re.IGNORECASE | re.MULTILINE)
    instruction = re.sub(r'^\*\*\[Question\s*\d+\]:\*\*\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^\*\*\[Question\s*\d+\]\*\*:\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^###\s*New\s+Coding\s+Assessment\s+Question\s*\n\s*\*\*\[Question\s*\d+\]:\*\*\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^###\s*New\s+Coding\s+Assessment\s+Question\s*\n\s*', '', instruction, flags=re.IGNORECASE)
    
    # Extract between specific delimiters if present
    match = re.search(r'<\|Question Begin\|>(.*?)<\|Question End\|>', instruction, re.DOTALL)
    if match:
        instruction = match.group(1).strip()

    # Remove leading : if present
    instruction = re.sub(r'^:\s*', '', instruction, flags=re.IGNORECASE)
    # Removing "Coding Assessment Question"
    instruction = re.sub(r'^Coding Assessment Question\s*\d*:\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^###\s*Coding\s+Assessment\s+Question:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^###\s*Problem\s+Statement:?\s*', '', instruction, flags=re.IGNORECASE)
    instruction = re.sub(r'^###\s*Coding\s+Question:?\s*', '', instruction, flags=re.IGNORECASE)
    # Remove leading and trailing whitespace
    instruction = instruction.strip()
    
    return instruction

def extract_instructions(input_file, output_file):
    """
    Extracts instructions from the assistant messages and saves them to an output file.
    """
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in tqdm(f_in, desc="Extracting Instructions"):
            data = json.loads(line)
            messages = data.get("messages", [])
            assistant_message = next((msg for msg in messages if msg["role"] == "assistant"), None)
            if not assistant_message:
                print("No assistant message found. Skipping.")
                continue

            instruction = extract_instruction(assistant_message["content"])
            if not instruction:
                print("Empty instruction after extraction. Skipping.")
                continue

            if "BAD_DOCUMENT" in instruction:
                print("BAD_DOCUMENT found. Skipping.")
                continue

            # Prepare the result structure
            result = {
                "instruction": instruction,
                "metadata": data.get("metadata", {})
            }

            f_out.write(json.dumps(result) + '\n')
            
    print(f"Finished extracting instructions. Output saved to {output_file}")

def sanitize_instructions(input_file, output_file, sentence_model, encoding_batch_size, distance_threshold, search_space_size, search_batch_size, device):
    """
    Sanitizes instructions by removing duplicates based on L2 distance.
    """
    ################
    # Step 1 - Load and Prepare the Dataset
    ################
    print(f"Loading dataset from {input_file}...")
    dataset = load_dataset("json", data_files=input_file, split='train')
    instructions = dataset["instruction"]
    print(f"Number of instructions: {len(instructions)}")

    ################
    # Step 2 - Encode Instructions
    ################
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer(sentence_model)
    model.to(device)

    print("Encoding instructions into embeddings...")
    embeddings = model.encode(instructions, batch_size=encoding_batch_size, convert_to_numpy=True, show_progress_bar=True)
    print(f"Embeddings shape: {embeddings.shape}")

    ################
    # Step 3 - Build Faiss Index
    ################
    print("Building Faiss index...")
    dimension = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)  # L2 distance
    faiss_index.add(embeddings)  # Remove normalization
    print(f"Faiss index has {faiss_index.ntotal} vectors.")

    ################
    # Step 4 - Find Similar Instructions
    ################
    print("Searching for similar instructions...")
    batch_size = search_batch_size
    k = search_space_size + 1  # +1 to include the instruction itself
    similar_indices = []
    similar_scores = []

    for i in tqdm(range(0, len(embeddings), batch_size), desc="Searching Batches"):
        end = min(i + batch_size, len(embeddings))
        batch = embeddings[i:end]
        scores, indices = faiss_index.search(batch, k)
        similar_indices.append(indices)
        similar_scores.append(scores)

    similar_indices = np.vstack(similar_indices)
    similar_scores = np.vstack(similar_scores)

    ################
    # Step 5 - Apply Threshold and Update Dataset
    ################
    print("Applying similarity threshold and updating dataset...")
    
    row_ids = [item.get("row_id", None) for item in dataset["metadata"]] if "metadata" in dataset.features else [None] * len(instructions)
    min_distances = {}
    duplicate_counts = {}
    min_similar_row_ids = {}

    for idx in tqdm(range(len(instructions)), desc="Processing Instructions"):
        similar = similar_indices[idx]
        scores = similar_scores[idx]
        
        # Find similar instructions (excluding self)
        self_idx = np.where(similar == idx)[0][0]
        similar_filtered = np.delete(similar, self_idx)
        scores_filtered = np.delete(scores, self_idx)
        
        # Count duplicates and find minimum distance
        filtered_indices = [index for index, score in zip(similar_filtered, scores_filtered) 
                          if score < distance_threshold]
        
        duplicate_count = len(filtered_indices)
        min_distance = float(scores_filtered[0])
        
        min_distances[idx] = min_distance
        duplicate_counts[idx] = duplicate_count
        
        if len(scores_filtered) > 0:
            min_similar_row_ids[idx] = row_ids[similar_filtered[np.argmin(scores_filtered)]]

    ################
    # Step 6 - Save Sanitized Instructions
    ################
    print("Saving sanitized instructions...")
    
    has_metadata = "metadata" in dataset.features
    metadata_list = dataset["metadata"] if has_metadata else [{}] * len(instructions)
    
    # Save all instructions
    all_output = output_file.replace('_sanitized.jsonl', '_all.jsonl')
    total_rows = 0
    with open(all_output, 'w') as f_out:
        for idx in tqdm(range(len(instructions)), desc="Preparing all entries"):
            entry = {
                "instruction": instructions[idx],
                "metadata": metadata_list[idx],
                "min_distance": min_distances[idx],
                "duplicate_count": duplicate_counts[idx],
                "min_similar_row_id": min_similar_row_ids[idx]
            }
            f_out.write(json.dumps(entry) + '\n')
            total_rows += 1
    print(f"Wrote {total_rows} rows to {all_output}")

    # Save filtered instructions
    filtered_rows = 0
    with open(output_file, 'w') as f_out:
        for idx in tqdm(range(len(instructions)), desc="Preparing filtered entries"):
            # Filter conditions: min_distance > threshold OR min_similar_row_id is self
            if min_distances[idx] > distance_threshold or min_similar_row_ids[idx] == row_ids[idx]:
                entry = {
                    "instruction": instructions[idx],
                    "metadata": metadata_list[idx],
                    "min_distance": min_distances[idx],
                    "duplicate_count": duplicate_counts[idx],
                    "min_similar_row_id": min_similar_row_ids[idx]
                }
                f_out.write(json.dumps(entry) + '\n')
                filtered_rows += 1
    print(f"Wrote {filtered_rows} rows to {output_file}")

    print(f"Sanitized instructions saved to {output_file}")
    print("Sanitization process completed.")

def prepare_instructions(input_file, output_file):
    """
    Prepares instructions by formatting them with prompts for response generation.
    """
    print(f"Preparing instructions from {input_file}")
    with open(input_file, 'r') as f, open(output_file, 'w') as outf:
        for line in tqdm(f, desc="Preparing Instructions"):
            data = json.loads(line)
            result = {
                "messages": [
                    {
                        "role": "user", 
                        "content": get_prompt(data["instruction"])
                    }
                ],
                "metadata": {
                    **data["metadata"],
                    "instruction": data["instruction"]
                }
            }
            outf.write(json.dumps(result) + "\n")
    print(f"Finished preparing instructions. Output saved to {output_file}")

def main():
    args = get_args()
    print(f"Instruction Processing Pipeline. Arguments: {args}")

    input_dir = os.path.dirname(args.input_file)
    input_basename = os.path.basename(args.input_file)
    print(f"Input directory: {input_dir}")
    print(f"Input basename: {input_basename}")
    
    # Define output paths
    if "prefill" in input_basename.lower():
        extracted_output = os.path.join(input_dir, input_basename.replace('seeds2questions', 'questions2sv').replace('_results', ''))
    else:
        extracted_output = os.path.join(input_dir, input_basename.replace('_prefill', '_questions2sv_prefill')).replace('_results', '')
    sanitized_output = extracted_output.replace('.jsonl', '_sanitized.jsonl')
    prepared_output = sanitized_output.replace('.jsonl', '_prepared.jsonl')

    # Run all steps in sequence
    extract_instructions(args.input_file, extracted_output)
    sanitize_instructions(
        input_file=extracted_output,
        output_file=sanitized_output,
        sentence_model=args.sentence_model,
        encoding_batch_size=args.encoding_batch_size,
        distance_threshold=args.distance_threshold,
        search_space_size=args.search_space_size,
        search_batch_size=args.search_batch_size,
        device=args.device
    )
    prepare_instructions(sanitized_output, prepared_output)

if __name__ == "__main__":
    main()