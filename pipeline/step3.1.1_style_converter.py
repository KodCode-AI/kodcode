import os
import sys
import csv
import argparse
import json
from tqdm import tqdm
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
from utils import *

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Style Conversion Manager.")
    parser.add_argument("--input_file", type=str, default=None)
    parser.add_argument("--output_folder_prefix", type=str, default="../demo")
    
    return parser.parse_args()

args = get_args() 
print(f"Arguments: {args}") # For logging

if args.input_file is None:
    raise ValueError("Input file is required")

# Create output folder if not exists
input_file_name = os.path.basename(args.input_file).split(".")[0]
args.output_folder = os.path.join(args.output_folder_prefix, f"Complete_{input_file_name}")
os.makedirs(args.output_folder, exist_ok=True)

def get_prompt(instruction, unit_test, solution):
    env = Environment(loader=FileSystemLoader('prompts'))
    template = env.get_template('gen_instruct_to_complete.md').render()
    
    # replace placeholder with instruction
    template = template.replace('[Coding Task Placeholder]', instruction)
    template = template.replace('[Unit Test Placeholder]', unit_test)
    template = template.replace('[Solution Placeholder]', solution)
    
    return template


# Get input file path and create output path in same directory
input_file = args.input_file
output_filename = os.path.join(args.output_folder, os.path.basename(input_file).replace(".json", "_i2c_prepared.jsonl"))

# Read the input problems
input_data = load_dataset_from_file(input_file)
for data in tqdm(input_data):
    result = {
        "messages": [
            {
                "role": "user", 
                "content": get_prompt(data["instruction"], data["test_code"], data["response"])
            }
        ],
        "metadata": {
            "instruction": data["instruction"],
            "response": data["response"],   
            "test_code": data["test_code"],
            "trials": data["trials"],
            "pass_sequence": data["pass_sequence"],
            "pass_trial_num": data["pass_trial_num"],
            "chosen_trial": data["chosen_trial"],
            "metadata": data["metadata"]
        }
    }
    with open(output_filename, "a") as outf:
        outf.write(json.dumps(result) + "\n")

print(f"Finished processing instructions from {input_file}")