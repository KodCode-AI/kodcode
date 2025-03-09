import os
import sys
import csv
import argparse
import json
from tqdm import tqdm
from collections import defaultdict
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from jinja2 import Environment, FileSystemLoader, exceptions

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Unit Test Generation Manager.")
    parser.add_argument("--test_folder", type=str)
    parser.add_argument("--output_folder", type=str, default="../demo")
    parser.add_argument("--save_to", type=str, default="json")
    
    return parser.parse_args()

args = get_args() 
print(f"Arguments: {args}") # For logging

if args.test_folder is None:
    raise ValueError("test_folder is required.")

def get_prompt(instruction):
    env = Environment(loader=FileSystemLoader('prompts'))
    template = env.get_template('gen_responses.md').render()
    # Add instruction to template
    template += instruction
    
    return template

# Stats tracking
total_count = 0
pass_sequence_collection = []

# Prepare output file path
output_file_base = "Verified"
output_fail_file_base = "Failed"
unit_test_name = os.path.basename(args.test_folder).replace("self_verification_", "")
output_file = f"{args.output_folder}/{output_file_base}_{unit_test_name}.{args.save_to}"
output_fail_file = f"{args.output_folder}/{output_fail_file_base}_{unit_test_name}_prepared.jsonl"

# Clear output files if they exist
if os.path.exists(output_file):
    os.remove(output_file)
if os.path.exists(output_fail_file):
    os.remove(output_fail_file)

if args.save_to != 'jsonl' and os.path.exists(output_file):
    with open(output_file, 'r') as f:
        aggregated_data = json.load(f)
else:
    aggregated_data = [] if args.save_to != 'jsonl' else None

# Iterate over each prompt directory (problem id) in unit_test_folder
for prompt_dir in tqdm(sorted(os.listdir(args.test_folder))):
    prompt_path = os.path.join(args.test_folder, prompt_dir)
    if not os.path.isdir(prompt_path):
        continue
    
    total_count += 1
    pass_trial_num = 0
    chosen_passing_test_coverage = 0
    problem_data = None
    trials_data = {}
    chosen_passing_solution = None
    chosen_passing_test = None
    
    # Track pass/fail sequence for this problem
    pass_sequence = []
    instruction_from_file = None
    
    # Iterate through each trial folder
    for trial_dir in sorted(os.listdir(prompt_path)):
        if not trial_dir.startswith('trial_'):
            continue
        
        trial_path = os.path.join(prompt_path, trial_dir)
        test_result_path = os.path.join(trial_path, "test_result.txt")
        data_json_path = os.path.join(trial_path, "data.json")
        
        if not os.path.exists(test_result_path):
            print(f"Test result not found for trial {trial_dir} in problem {prompt_dir}")
            continue
        if not os.path.exists(data_json_path):
            print(f"data.json not found for trial {trial_dir} in problem {prompt_dir}")
            continue

        with open(test_result_path, 'r') as f:
            test_result_lines = f.read().strip().split('\n')
            test_result = test_result_lines[0]
            try:
                test_coverage = float(test_result_lines[1].split(': ')[1].strip('%')) if len(test_result_lines) > 1 else None
            except:
                test_coverage = None
        
        with open(data_json_path, 'r') as f:
            try:
                data_json = json.load(f)
            except:
                print(f"Error loading {data_json_path}")
                continue

        # Sanity check: instruction should be the same for all trials
        if 'instruction' in data_json:
            if instruction_from_file is None:
                instruction_from_file = data_json["instruction"]
            else:
                if instruction_from_file != data_json["instruction"]:
                    raise ValueError(f"Instruction mismatch in {prompt_dir} and {trial_dir}")
            
        # Store trial data
        try:
            trial_data = {
                "solution_code": data_json["solution_code"],
                "test_code": data_json["test_code"],
                "test_result": test_result,
                "test_coverage": test_coverage,
                "file_source": data_json["file_source"]
            }
        except Exception as e:
            print(f"Error in {data_json_path}: {e}")
            continue
        
        trials_data[trial_dir] = trial_data
        
        # Track pass/fail sequence
        pass_sequence.append(1 if test_result == "Pass" else 0)
        
        # Store first passing solution
        if test_result == "Pass":
            pass_trial_num += 1
            if test_coverage == 100.0:
                chosen_passing_solution = data_json["solution_code"]
                chosen_passing_test = data_json["test_code"]
                chosen_passing_test_coverage = test_coverage
                chosen_passing_trial_key = trial_dir
            elif chosen_passing_solution is None or (test_coverage is not None and test_coverage > chosen_passing_test_coverage):
                chosen_passing_solution = data_json["solution_code"]
                chosen_passing_test = data_json["test_code"]
                chosen_passing_test_coverage = test_coverage if test_coverage is not None else 0
                chosen_passing_trial_key = trial_dir
    
    # pass@k statistics
    pass_sequence_collection.append(pass_sequence)

    # Prepare responses
    if not trials_data:
        print(f"No trials data for problem {prompt_dir}. Skipping...")
        continue
    elif chosen_passing_solution is None:
        try:
            problem_data = {
                "messages": [
                    {
                        "role": "user", 
                        "content": get_prompt(data_json["instruction"])
                    }
                ],
                "metadata": {
                    **data_json["metadata"],
                    "pass_sequence": pass_sequence,
                }
            }
        except Exception as e:
            print(f"Error in {prompt_dir}: {e}")
            continue

        with open(output_fail_file, 'a') as outf:
            outf.write(json.dumps(problem_data) + "\n")
    else: # At least one passing solution
        # Use the chosen passing solution as the response
        response = chosen_passing_solution
        test_code = chosen_passing_test
            
        # Store problem data (only need to do this once)
        try:
            problem_data = {
                "instruction": data_json["instruction"],
                "response": response,
                "test_code":  test_code,
                "trials": trials_data,
                "pass_sequence": pass_sequence,
                "pass_trial_num": pass_trial_num,
                "chosen_trial": chosen_passing_trial_key if chosen_passing_solution is not None else chosen_trial_key,
                "metadata": data_json["metadata"]
            }
        except Exception as e:
            print(f"Error in {prompt_dir}: {e}")
            continue
        
        # Aggregate data
        if args.save_to == 'jsonl':
            with open(output_file, 'a') as outf:
                outf.write(json.dumps(problem_data) + "\n")
        else:
            aggregated_data.append(problem_data)

# If not saving as jsonl, write aggregated data to output file
if args.save_to != 'jsonl':
    with open(output_file, 'w') as outf:
        json.dump(aggregated_data, outf, indent=2)

print(f"Finished processing data from {args.test_folder}.")
print(f"Output File Path: {output_file}")
print(f"\nStats:")
print(f"Total examples processed: {total_count}")

print("\nPass@k Statistics:")
pass_at_k = {}
samples_at_k = {}

# Calculate pass@k statistics
max_k = max(len(sequence) for sequence in pass_sequence_collection)
print(f"Max k: {max_k}")
for k in range(1, max_k + 1): 
    pass_at_k[k] = 0
    samples_at_k[k] = 0
    for sequence in pass_sequence_collection:
        # Only count sequences long enough for k
        if len(sequence) >= k:
            samples_at_k[k] += 1
        
        # Check if there's at least one pass in first k trials
        if 1 in sequence[:k]:
            pass_at_k[k] += 1

# Print pass@k results
for k in sorted(pass_at_k.keys()):
    if samples_at_k[k] > 0:
        success_rate = (pass_at_k[k] / total_count) * 100
        print(f"Pass@{k}: {success_rate:.2f}% ({pass_at_k[k]}/{total_count})")

# Print samples at k
for k in sorted(samples_at_k.keys()):
    print(f"Samples at {k}: {samples_at_k[k]}")

# Save Pass@K and Pass Count Distribution to a file
with open(f"{args.output_folder}/pass_at_k_{unit_test_name}.json", 'w') as f:
    json.dump({
        "pass_at_k": pass_at_k,
        "total_count": total_count
    }, f, indent=2)

# Save the data to a CSV file
csv_file_path = f"{args.output_folder}/pass_at_k_{unit_test_name}.csv"
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write Pass@K statistics
    csv_writer.writerow(["Pass@K", "Percentage", "Pass Count"])
    for k in sorted(pass_at_k.keys()):
        rate = (pass_at_k[k] / total_count) * 100
        csv_writer.writerow([f"Pass@{k}", f"{rate:.2f}%", pass_at_k[k]])
