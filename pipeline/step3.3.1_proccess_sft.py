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
from utils import load_dataset_from_file
################
# Configurations
################
def get_args():
    parser = argparse.ArgumentParser(description="Instruction Processing Manager.")
    
    # Input Parameters
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input JSONL file.")
    parser.add_argument("--output_folder", type=str, default="../demo", help="Path to the output folder.")
    return parser.parse_args()

def prepare_questions(input_file, output_file):
    """
    Prepares questions by formatting them with prompts for response generation.
    """
    print(f"Preparing questions from {input_file}")
    input_data = load_dataset_from_file(input_file)

    with open(output_file, 'w') as outf:
        for data in tqdm(input_data, desc="Preparing Questions"):
            # Follow the format of KodCode-V1-SFT-R1: https://huggingface.co/datasets/KodCode/KodCode-V1-SFT-R1
            result = {
                "messages": [
                    {
                        "role": "user", 
                        "content": data["question"]
                    }
                ],
                "metadata": {
                    "style": data["style"],
                    "subset": data["subset"],
                    "question_id": data["question_id"],
                    "question": data["question"],
                    "solution": data["solution"],
                    "test_code": data["test_code"],
                    "test_info": data["test_info"],
                    "gpt_pass_sequence": data["gpt_pass_sequence"],
                    "gpt_pass_trial_num": data["gpt_pass_trial_num"],
                    "gpt_difficulty": data["gpt_difficulty"],
                    "gpt_pass_percentage": data["gpt_pass_percentage"],
                    "metadata": data["metadata"]
                }
            }
            outf.write(json.dumps(result) + "\n")
    print(f"Finished preparing instructions. Output saved to {output_file}")

def main():
    args = get_args()
    print(f"Instruction Processing Pipeline. Arguments: {args}")
    file_basename = os.path.basename(args.input_file).replace('.json', '')
    output_file = os.path.join(args.output_folder, f"SFT_{file_basename}/{file_basename}_prepared.jsonl")

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    prepare_questions(args.input_file, output_file)

if __name__ == "__main__":
    main()