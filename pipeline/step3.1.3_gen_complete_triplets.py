import os
import sys
import csv
import argparse
import json
import re
from tqdm import tqdm
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
from utils import *

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Unit Test Generation Manager.")
    parser.add_argument("--input_file", type=str, default=None)
    
    return parser.parse_args()

args = get_args() 
print(f"Arguments: {args}") # For logging

if args.input_file is None:
    raise ValueError("Input file is required.")

# Obtain the output folder from the input file
args.output_folder = os.path.dirname(args.input_file)

# Read the completion set
completion_set = load_dataset_from_file(args.input_file)
print(f"Length of completion set: {len(completion_set)}")

# Create a new list to store the saved results
saved_results = []

# Process each completion entry
for completion_entry in tqdm(completion_set):

    assistant_message = next((msg for msg in completion_entry["messages"] if msg["role"] == "assistant"), None)
    content = assistant_message["content"]
    completion_match = re.search(r'<\|Completion Begin\|>(.*?)<\|Completion End\|>', content, re.DOTALL)
    
    if completion_match is None:
        print(f"No completion match found for prompt_id: {completion_entry['metadata']['metadata']['prompt_id']}")
        continue
    else:
        # Create a new merged entry based on the instruction
        completion_match_content = completion_match.group(1).strip().replace('```python\n', '').replace('```', '').strip()
        # Sanity check to make sure the completion match content is not the same as the response
        if completion_match_content == completion_entry["metadata"]["response"]:
            print(f"Completion match content == response for prompt_id: {completion_entry['metadata']['metadata']['prompt_id']}")
            continue
        else:
            saved_entry = {
                "instruction": completion_match_content,
                "response": completion_entry["metadata"]["response"],
                "test_code": completion_entry["metadata"]["test_code"],
                "trials": completion_entry["metadata"]["trials"],
                "pass_sequence": completion_entry["metadata"]["pass_sequence"],
                "pass_trial_num": completion_entry["metadata"]["pass_trial_num"],
                "chosen_trial": completion_entry["metadata"]["chosen_trial"],
                "metadata": completion_entry["metadata"]["metadata"]
            }
            # Add the original instruction to the metadata
            saved_entry["metadata"]["original_instruction"] = completion_entry["metadata"]["instruction"]

            saved_results.append(saved_entry)


# Save the merged results to a new file
output_file = os.path.join(args.output_folder, os.path.basename(args.input_file).replace("_i2c_prepared_results.jsonl", "_Complete.json"))
save_dataset(saved_results, output_file)

print(f"Processed {len(saved_results)} matched entries")