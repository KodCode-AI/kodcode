import os
import sys
import argparse
import json
import re
import csv
from tqdm import tqdm
from collections import defaultdict

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="Dataset Generation Manager.")
    parser.add_argument("--unit_test_folder", type=str, default="../unit_test")
    parser.add_argument("--output_folder", type=str, default="../demo")
    parser.add_argument("--save_to", type=str, default="json")
    
    return parser.parse_args()

args = get_args() 
print(f"Arguments: {args}") # For logging

# Stats tracking
id = 0
total_count = 0
pass_at_k = defaultdict(int)  # Track pass@k statistics
pass_count_dist = defaultdict(int)  # Track distribution of number of passes
samples_at_k = defaultdict(int)  # Track number of samples for each k

# Prepare output file path
unit_test_name = os.path.basename(args.unit_test_folder).replace("cross_verification_", "")
output_file_name = os.path.basename(args.unit_test_folder).replace("cross_verification_", "")
output_file = os.path.join(args.output_folder, f"{output_file_name}.{args.save_to}")

aggregated_data = []

# Iterate over each prompt directory (problem id) in unit_test_folder
for prompt_dir in tqdm(sorted(os.listdir(args.unit_test_folder))):
    prompt_path = os.path.join(args.unit_test_folder, prompt_dir)
    if not os.path.isdir(prompt_path):
        continue
    
    total_count += 1
    pass_trial_num = 0
    chosen_passing_test_coverage = 0
    problem_data = None
    trials_data = {}
    chosen_passing_solution = None
    chosen_passing_test = None
    chosen_passing_response = None
    
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
        if 'question' in data_json:
            if instruction_from_file is None:
                instruction_from_file = data_json["question"]
            else:
                if instruction_from_file != data_json["question"]:
                    raise ValueError(f"Question mismatch in {prompt_dir} and {trial_dir}")
            
        # Store trial data
        try:
            trial_data = {
                "r1_response": data_json["r1_response"],
                "r1_solution": data_json["r1_solution"],
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
                chosen_passing_solution = data_json["r1_solution"]
                chosen_passing_test = data_json["test_code"]
                chosen_passing_response = data_json["r1_response"]
                chosen_passing_test_coverage = test_coverage
                chosen_passing_trial_key = trial_dir
            elif chosen_passing_solution is None or (test_coverage is not None and test_coverage > chosen_passing_test_coverage):
                chosen_passing_solution = data_json["r1_solution"]
                chosen_passing_test = data_json["test_code"]
                chosen_passing_response = data_json["r1_response"]
                chosen_passing_test_coverage = test_coverage if test_coverage is not None else 0
                chosen_passing_trial_key = trial_dir

    assert pass_trial_num==sum(pass_sequence)

    # pass@k statistics
    has_passed = False
    for k in range(1, len(pass_sequence) + 1):
        samples_at_k[k] += 1  # Count this sample for this k
        has_passed = has_passed or any(pass_sequence[:k])
        if has_passed:
            pass_at_k[k] += 1

    # Update pass count distribution
    total_passes = sum(pass_sequence)
    pass_count_dist[total_passes] += 1

    # Prepare responses
    if not trials_data:  # Add check for empty trials_data
        print(f"Warning: No valid trials found for problem {prompt_dir}")
        continue  # Skip this problem
        
    if chosen_passing_solution is None:
        # Use the first solution as the response
        chosen_trial_key = next(iter(trials_data))
        response = trials_data[chosen_trial_key]["r1_response"]
        test_code = trials_data[chosen_trial_key]["test_code"]
        solution = trials_data[chosen_trial_key]["r1_solution"]
    else:
        # Use the first passing solution as the response
        chosen_trial_key = chosen_passing_trial_key
        response = chosen_passing_response
        test_code = chosen_passing_test
        solution = chosen_passing_solution

    conversations = [
        {"from": "human", "value": data_json["question"]},
        {"from": "gpt", "value": response}
    ]

    problem_data = {
        "style": data_json["style"],
        "subset": data_json["subset"],
        "question_id": data_json["question_id"],
        "question": data_json["question"],
        "solution": data_json["solution"],
        "test_code": data_json["test_code"],
        "test_info": data_json["test_info"],
        "gpt_pass_sequence": data_json["gpt_pass_sequence"],
        "gpt_pass_trial_num": data_json["gpt_pass_trial_num"],
        "gpt_difficulty": data_json["gpt_difficulty"],
        "gpt_pass_percentage": data_json["gpt_pass_percentage"],
        "r1_solution": solution,
        "r1_pass_sequence": pass_sequence,
        "r1_pass_trial_num": pass_trial_num,
        "r1_correctness": "True" if pass_trial_num > 0 else "False",
        "r1_chosen_trial_key": chosen_trial_key,
        "metadata": data_json["metadata"],
        "conversations": conversations
    }
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

print(f"Finished processing data from {args.unit_test_folder}.")
print(f"Output File Path: {output_file}")
print(f"\nStats:")
print(f"Total examples processed: {total_count}")

print("\nPass@k Statistics:")
for k in sorted(pass_at_k.keys()):
    rate = (pass_at_k[k] / samples_at_k[k]) * 100 # Use the corresponding samples_at_k
    print(f"Pass@{k}: {rate:.2f}% ({pass_at_k[k]}/{samples_at_k[k]} examples)")

print("\nPass Count Distribution:")
for count in sorted(pass_count_dist.keys()):
    rate = (pass_count_dist[count] / total_count) * 100
    print(f"{count} passes: {rate:.2f}% ({pass_count_dist[count]} examples)")


stats_file_path = os.path.dirname(args.unit_test_folder)
# Save Pass@K and Pass Count Distribution to a file
with open(os.path.join(stats_file_path, f"pass_at_k_{unit_test_name}.json"), 'w') as f:
    json.dump({
        "pass_at_k": pass_at_k,
        "total_count": total_count
    }, f, indent=2)

# Save the data to a CSV file
csv_file_path = os.path.join(stats_file_path, f"pass_at_k_{unit_test_name}.csv")
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write Pass@K statistics
    csv_writer.writerow(["Pass@K", "Percentage", "Pass Count"])
    for k in sorted(pass_at_k.keys()):
        rate = (pass_at_k[k] / total_count) * 100
        csv_writer.writerow([f"Pass@{k}", f"{rate:.2f}%", pass_at_k[k]])
