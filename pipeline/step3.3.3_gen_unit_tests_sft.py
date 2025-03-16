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
    parser.add_argument("--output_folder_prefix", type=str, default="cross_verification")
    parser.add_argument("--model_nickname", type=str, default="r1")
    parser.add_argument("--replace_function_name", type=bool, default=True)

    return parser.parse_args()

args = get_args()
print(f"Unit Test Generation Manager. Arguments: {args}") # For logging

# Find all input files ending with _sanitized_prepared_results*.jsonl
input_files = glob.glob(os.path.join(args.input_folder, "*_prepared_results*.jsonl"))
print(f"Found {len(input_files)} input files: {input_files}")

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
                raise ValueError("No user message found.")        
            if assistant_message is None:
                print("No assistant message found.")
                continue

            # Obtain test code and entry point info
            test_code = generated_data["metadata"]["test_code"]
            try:
                if len(generated_data["metadata"]["test_info"]) == 1:
                    entry_point = generated_data["metadata"]["test_info"][0]["function_name"]
                else:
                    entry_point = None
            except:
                entry_point = None

            # Get trial number and prompt id
            file_basename = os.path.basename(input_file)
            trial_num = int(re.search(r'prepared_results(\d+)', file_basename).group(1))
            question_id = generated_data["metadata"]["question_id"]

            # Extract solution code from assistant message
            content = assistant_message["content"]
            solution_match = re.search(r'</think>(.*)', content, re.DOTALL) # We skip thinking process
            if solution_match:
                solution_code_match = re.search(r'```python(.*?)```', solution_match.group(1), re.DOTALL)
                if solution_code_match:
                    solution_code = solution_code_match.group(1).strip()
                    # Extract and replace function name in solution code
                    solution_func_match = re.search(r'def\s+(\w+)\s*\(', solution_code)

                    # If the function name is changed, replace it with the entry point
                    if solution_func_match and args.replace_function_name and len(re.findall(r'def\s+\w+\s*\(', solution_code)) == 1:
                        old_func_name = solution_func_match.group(1)
                        if entry_point and entry_point != old_func_name:
                            solution_code = solution_code.replace(f"def {old_func_name}", f"def {entry_point}")
                            print(f"Function Name Changed from {old_func_name} to {entry_point} for question_id {question_id}, trial_num {trial_num}.")
                    
                    # Create folder for this test case
                    test_folder = os.path.join(f"{args.input_folder}/{args.output_folder_prefix}_{folder_basename}", question_id, f"trial_{args.model_nickname}_{trial_num}")
                    
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
                        "style": generated_data["metadata"]["style"],
                        "subset": generated_data["metadata"]["subset"],
                        "question_id": generated_data["metadata"]["question_id"],
                        "question": generated_data["metadata"]["question"],
                        "solution": generated_data["metadata"]["solution"],
                        "test_code": generated_data["metadata"]["test_code"],
                        "test_info": generated_data["metadata"]["test_info"],
                        "gpt_pass_sequence": generated_data["metadata"]["gpt_pass_sequence"],
                        "gpt_pass_trial_num": generated_data["metadata"]["gpt_pass_trial_num"],
                        "gpt_difficulty": generated_data["metadata"]["gpt_difficulty"],
                        "gpt_pass_percentage": generated_data["metadata"]["gpt_pass_percentage"],
                        "r1_response": content,
                        "r1_solution": solution_code,
                        "metadata": generated_data["metadata"]["metadata"],
                        "file_source": file_basename
                    }
                    if "gen_response_configs" in generated_data:
                        processed_data["gen_response_configs"] = generated_data["gen_response_configs"]
                    with open(os.path.join(test_folder, "data.json"), "w") as f:
                        json.dump(processed_data, f, indent=2)
                else:
                    print(f"No solution code found in response with question_id {question_id} and trial_num {trial_num}.")
                    continue

print(f"Finished processing all input files.")
