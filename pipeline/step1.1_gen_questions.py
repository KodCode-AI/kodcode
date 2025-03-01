import torch
import os
import sys
import argparse
import json
import time
import random
import numpy as np
from tqdm import tqdm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transformers import AutoTokenizer, AutoModelForCausalLM
from jinja2 import Environment, FileSystemLoader, exceptions

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Seed Generation Manager.")
    # Generation Parameters
    parser.add_argument("--total_prompts", type=int, default=1000, help="Total number of prompts to generate. If specified, repeat will be ignored.")
    parser.add_argument('--mode', default="leetcode", type=str, choices=["leetcode", "algorithm", "data_structure", "package", "apps", "codeforces", "code_contests", "taco", "docs"])

    # System Settings
    parser.add_argument("--output_folder", type=str, default="../data_step1")
    parser.add_argument("--job_name", type=str, default=None, help="Job Name.")
    parser.add_argument("--timestamp", type=int, default=int(time.time()), help="Timestamp for the job. Also used as the random seed.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed.")

    return parser.parse_args()

def get_seed_prompt(input, mode):
    # Load prompt template from markdown file
    env = Environment(loader=FileSystemLoader('prompts'))
    
    if mode in ["leetcode", "codeforces"]:
        template = env.get_template('genq_from_seed.md').render()
        # Add sample questions
        for i, problem in enumerate(input, 1):
            template += f"[Question {i}]: {problem['description']}\n\n"
        
        template += f"[Question {len(input) + 1}]:"
        
    elif mode in ["algorithm", "data_structure"]:
        template = env.get_template('genq_from_snippets.md').render()
        # Add code snippets section
        template += "\n```python\n"
        template += input[0]['codes'] + "\n"
        template += "```"
    
    elif mode == "docs":
        template = env.get_template('genq_from_docs.md').render()
        # Add code snippets section
        template = template.replace("{PACKAGE_NAME}", input[0]['source_name'])
        template = template.replace("{CONTENT}", input[0]['content'])

    elif mode in ["package", "apps", "taco", "code_contests"]:
        template = env.get_template('genq_from_seed.md').render()
        # Add sample questions
        for i, problem in enumerate(input, 1):
            template += f"[Question {i}]: {problem['instruction']}\n\n"
        
        template += f"[Question {len(input) + 1}]:"
    
    return template

args = get_args()
print(f"Instruction Generation Manager. Arguments: {args}") # For logging

# Set the random seed for NumPy
if args.seed is not None:
    np.random.seed(args.seed)
    # Set the random seed for PyTorch
    torch.manual_seed(args.seed)
    # If you are using CUDA (i.e., a GPU), also set the seed for it
    torch.cuda.manual_seed_all(args.seed)

# Create output file / folder
output_filename = f"CodeGen_seed_{args.mode}_{args.total_prompts}_{args.timestamp}.jsonl"
output_foldername = f"CodeGen_{args.mode}_{args.total_prompts}_{args.timestamp}"
if not args.job_name:
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    if not os.path.exists(f"{args.output_folder}/{output_foldername}"):
        os.makedirs(f"{args.output_folder}/{output_foldername}")
    output_dir = f"{args.output_folder}/{output_foldername}/{output_filename}"
else:
    output_dir = f"{args.output_folder}/{args.job_name}/{output_filename}"


# Read the seed problems
if args.mode == "leetcode":
    with open('../seeds/leetcode/leetcode-problems-reorganized.json', 'r') as f:
        seed_problems = json.load(f)
elif args.mode == "codeforces":
    with open('../seeds/codeforces/codeforces.jsonl', 'r') as f:
        seed_problems = [json.loads(line) for line in f]
        for i, problem in enumerate(seed_problems):
            problem['id'] = i
            problem['instruction'] = problem['problem_statement']
elif args.mode == "taco":
    with open('../seeds/taco/TACO_train_lite.json', 'r') as f:
        seed_problems = json.load(f)
        for i, problem in enumerate(seed_problems):
            problem['id'] = i
            problem['instruction'] = problem['question']
elif args.mode == "code_contests":
    with open('../seeds/code_contests/code_contests_train_lite.json', 'r') as f:
        seed_problems = json.load(f)
        for i, problem in enumerate(seed_problems):
            problem['id'] = i
            problem['instruction'] = problem['question']
elif args.mode == "package":
    with open('../seeds/package/package_instruct_train_2000.json', 'r') as f:
        seed_problems = json.load(f)
        # add id to each problem
        for i, problem in enumerate(seed_problems):
            problem['id'] = i
elif args.mode == "apps":
    with open('../seeds/apps/apps_train_lite.json', 'r') as f:
        seed_problems = json.load(f)
        for i, problem in enumerate(seed_problems):
            problem['id'] = problem['problem_id']
            problem['instruction'] = problem['question']
elif args.mode == "algorithm":
    with open('../seeds/algorithms/algorithm-python.json', 'r') as f:
        seed_problems = json.load(f)
elif args.mode == "data_structure":
    with open('../seeds/data_structure/data-structure-python.json', 'r') as f:
        seed_problems = json.load(f)
elif args.mode == "docs":
    with open('../seeds/docs/kodcode-docs.json', 'r') as f:
        seed_problems = json.load(f)

print(f"Number of seed files: {len(seed_problems)}")
################
# Generate outputs
################
results = []
for i in tqdm(range(args.total_prompts)):
    # Select 3 random problems (since it is too short)
    if args.mode in ["leetcode"]:
        selected_problems = random.sample(seed_problems, 3)
        seed_prompt = get_seed_prompt(selected_problems, args.mode)
    # For other modes, we only need 1 problem
    else:
        selected_problems = random.sample(seed_problems, 1)
        seed_prompt = get_seed_prompt(selected_problems, args.mode)

    # Save outputs      
    result = {
        "messages": [
            {
                "role": "user",
                "content": seed_prompt
            }
        ],
        "metadata": {
            "prompt_id": f"{i:08d}",
            "row_id": i,
            "problem_ids": [problem['id'] for problem in selected_problems],
            "mode": args.mode,
        },
    }
    results.append(result)

# Save the final results
with open(output_dir, "w") as f:
    for result in results:
        f.write(json.dumps(result) + "\n")

print(f"Finished. Total prompts: {len(results)}")
print(f"Output directory: {output_dir}")

