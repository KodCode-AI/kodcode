import torch
import os
import sys
import argparse
import json
import time
import random
import numpy as np
from tqdm import tqdm
import re
import glob
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Unit Test Generation Manager.")
    parser.add_argument("--input_folder", type=str, default=None)
    parser.add_argument("--output_folder_prefix", type=str, default="../unit_test_Step2")

    return parser.parse_args()

args = get_args()
print(f"Unit Test Generation Manager. Arguments: {args}") # For logging

# Find all input files ending with _combined
input_files = glob.glob(os.path.join(args.input_folder, "*_combined.jsonl"))
print(f"Found {len(input_files)} input files")

folder_basename = os.path.basename(args.input_folder.rstrip('/'))
print(f"Folder basename: {folder_basename}")

# Store instructions for verification
instructions = {}

# Process each input file
for input_file in input_files:
    print(f"Processing {input_file}")
    with open(input_file, 'r') as f:
        for line in tqdm(f):
            generated_data = json.loads(line)
            # Get the assistant message content as the instruction
            user_message = next((msg for msg in generated_data["messages"] if msg["role"] == "user"), None)
            assistant_message = next((msg for msg in generated_data["messages"] if msg["role"] == "assistant"), None)
            if user_message is None:
                raise ValueError("No user message found in seed data")        
            if assistant_message is None:
                print("No assistant message found in seed data")
                continue

            # get instruction from metadata if there is
            try:
                if "instruction" in generated_data["metadata"]:
                    instruction = generated_data["metadata"]["instruction"]
                    del generated_data["metadata"]["instruction"]
                else:
                    instruction = user_message["content"].split("<|Test End|>\n\n## Question:")[1].strip()
            except:
                print(f"No instruction found!")
                continue

            prompt_id = str(generated_data["metadata"]["prompt_id"])
            
            # Verify instruction consistency
            if prompt_id not in instructions:
                instructions[prompt_id] = instruction
            elif instructions[prompt_id] != instruction:
                raise ValueError(f"Inconsistent instructions found for prompt_id {prompt_id}")

            # Extract solution and test code from assistant message
            content = assistant_message["content"]
            solution_match = re.search(r'<\|Solution Begin\|>(.*?)<\|Solution End\|>', content, re.DOTALL)
            test_match = re.search(r'<\|Test Begin\|>(.*?)<\|Test End\|>', content, re.DOTALL)

            if solution_match and test_match:
                solution_code = solution_match.group(1).strip().replace('```python\n', '').replace('```', '').strip()
                test_code = test_match.group(1).strip().replace('```python\n', '').replace('```', '').strip()

                # Get trial number from input file name
                file_basename = os.path.basename(input_file)
                trial_num = int(re.search(r'prepared(\d+)_results', file_basename).group(1))
                
                # Create folder for this test case
                test_folder = os.path.join(f"{args.output_folder_prefix}_{folder_basename}", prompt_id, f"trial_gpt4o_{trial_num}")
                
                # Skip if the test folder already exists
                if os.path.exists(test_folder):
                    print(f"Skipping existing test folder: {test_folder}")
                    continue
                    
                os.makedirs(test_folder, exist_ok=True)

                # Write solution.py
                with open(os.path.join(test_folder, "solution.py"), "w") as f:
                    f.write(solution_code)

                # Write test_solution.py  
                with open(os.path.join(test_folder, "test_solution.py"), "w") as f:
                    f.write("from solution import *\n\n" + test_code)

                # Copy run_test.sh
                with open("run_test.sh", "r") as src:
                    with open(os.path.join(test_folder, "run_test.sh"), "w") as dst:
                        dst.write(src.read())
                        
                # Make run_test.sh executable
                os.chmod(os.path.join(test_folder, "run_test.sh"), 0o755)

                # Save processed data as JSON
                processed_data = {
                    "metadata": generated_data["metadata"],
                    "instruction": instruction,
                    "solution_code": solution_code,
                    "test_code": test_code,
                    "file_source": file_basename
                }
                if "gen_response_configs" in generated_data:
                    processed_data["gen_response_configs"] = generated_data["gen_response_configs"]
                with open(os.path.join(test_folder, "data.json"), "w") as f:
                    json.dump(processed_data, f, indent=2)

print(f"Finished processing all input files.")
