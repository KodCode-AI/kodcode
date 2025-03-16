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
    parser = argparse.ArgumentParser(description="KodCode Combination Manager.")
    parser.add_argument("--kodcode_exp_name", type=str, default=None)
    parser.add_argument("--output_folder", type=str, default="../demo")

    return parser.parse_args()

args = get_args() 
print(f"Arguments: {args}") # For logging

if args.kodcode_exp_name is None:
    raise ValueError("KodCode experiment name is required.")


# Read the instruction set
instruction_folder = os.path.join(args.output_folder, args.kodcode_exp_name)
instruction_file = os.path.join(instruction_folder, "Verified_" + args.kodcode_exp_name + ".json")
instruction_set = load_dataset_from_file(instruction_file)
print(f"Length of instruction set: {len(instruction_set)}")

# Read the completion set
completion_folder = os.path.join(args.output_folder, "Complete_Verified_" + args.kodcode_exp_name)
completion_file = os.path.join(completion_folder, "Verified_" + args.kodcode_exp_name + "_Complete.json")
completion_set = load_dataset_from_file(completion_file)
print(f"Length of completion set: {len(completion_set)}")


combined_results = []

# Process instruction entries
for instruction_entry in instruction_set:
    # Obtain the function info from the response
    if "class " not in instruction_entry['response'] and "__init__" not in instruction_entry['response']:
        function_info = extract_function_info_from_ast(instruction_entry["response"])
    else:
        function_info = None
    
    # Obtain the subset name, pass trial number, difficulty, and pass percentage of the GPT response
    subset_name = get_mode(instruction_entry["metadata"]["mode"]) 
    pass_trial_num = instruction_entry["pass_sequence"].count(1)
    gpt_difficulty = get_gpt_difficulty(instruction_entry["pass_sequence"])
    gpt_pass_percentage = get_gpt_pass_percentage(instruction_entry["pass_sequence"])

    # Assign empty original instruction
    instruction_entry["metadata"]["original_instruction"] = ""

    # Entry names are aligned with KodCode-V1: https://huggingface.co/datasets/KodCode/KodCode-V1
    saved_entry = {
        "style": "instruct",
        "subset": subset_name,
        "question_id": f"{subset_name}_{instruction_entry['metadata']['prompt_id']}_I",
        "question": instruction_entry["instruction"],
        "solution": instruction_entry["response"],
        "test_code": instruction_entry["test_code"],
        "test_info": function_info,
        "gpt_pass_sequence": instruction_entry["pass_sequence"],
        "gpt_pass_trial_num": pass_trial_num,
        "gpt_difficulty": gpt_difficulty,
        "gpt_pass_percentage": gpt_pass_percentage,
        "trials": instruction_entry["trials"],
        "chosen_trial": instruction_entry["chosen_trial"],
        "metadata": instruction_entry["metadata"]
    }
    
    combined_results.append(saved_entry)

# Process completion entries
for completion_entry in completion_set:
    # Obtain the function info from the response
    if "class " not in completion_entry['response'] and "__init__" not in completion_entry['response']:
        function_info = extract_function_info_from_ast(completion_entry["response"])
    else:
        function_info = None
    
    # Obtain the subset name, pass trial number, difficulty, and pass percentage of the GPT response
    subset_name = get_mode(completion_entry["metadata"]["mode"]) 
    pass_trial_num = completion_entry["pass_sequence"].count(1)
    gpt_difficulty = get_gpt_difficulty(completion_entry["pass_sequence"])
    gpt_pass_percentage = get_gpt_pass_percentage(completion_entry["pass_sequence"])

    # Entry names are aligned with KodCode-V1: https://huggingface.co/datasets/KodCode/KodCode-V1
    saved_entry = {
        "style": "instruct",
        "subset": subset_name,
        "question_id": f"{subset_name}_{completion_entry['metadata']['prompt_id']}_C",
        "question": completion_entry["instruction"],
        "solution": completion_entry["response"],
        "test_code": completion_entry["test_code"],
        "test_info": function_info,
        "gpt_pass_sequence": completion_entry["pass_sequence"],
        "gpt_pass_trial_num": pass_trial_num,
        "gpt_difficulty": gpt_difficulty,
        "gpt_pass_percentage": gpt_pass_percentage,
        "trials": completion_entry["trials"],
        "chosen_trial": completion_entry["chosen_trial"],
        "metadata": completion_entry["metadata"]
    }
    
    combined_results.append(saved_entry)

# Save the combined results to a new file
output_file = os.path.join(args.output_folder, f"{args.kodcode_exp_name}.json")
save_dataset(combined_results, output_file)

print(f"Combined {len(instruction_set)} instruction entries and {len(completion_set)} completion entries")
print(f"Total {len(combined_results)} entries saved to {output_file}")