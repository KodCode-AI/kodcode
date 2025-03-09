import argparse
from openai import OpenAI
import json
from tqdm import tqdm
from utils import load_dataset_from_file, save_dataset

client = OpenAI()

################
# Configurations
################
def get_args():
    # Experiment Settings
    parser = argparse.ArgumentParser(description="OpenAI API Call Manager.")
    # Generation Parameters
    parser.add_argument("--model", type=str, default="gpt-4o-2024-05-13", help="OpenAI model name.")
    parser.add_argument("--input_file", type=str, default="../data_step1/leetcode_questions.jsonl", help="Input file.")
    parser.add_argument("--temperature", type=float, default=0.0, help="Temperature for the API call.")
    parser.add_argument("--max_tokens", type=int, default=8192, help="Max tokens for the API call.")
    parser.add_argument("--top_p", type=float, default=1.0, help="Top p for the API call.")
    parser.add_argument("--num_trials", type=int, default=1, help="Number of trials to run.")
    return parser.parse_args()

args = get_args()

# Input check: check if ends with prepared.jsonl
if not args.input_file.endswith("prepared.jsonl"):
    print("Error: Input file must end with prepared.jsonl for KodCode pipeline. Please make sure you are using the correct input file.")
    exit(1)

if args.num_trials > 1:
    output_files = [args.input_file.replace(".jsonl", f"_results{i}.jsonl") for i in range(args.num_trials)]
else:
    output_file = args.input_file.replace(".jsonl", "_results.jsonl")

data = load_dataset_from_file(args.input_file)

for i in range(args.num_trials):
    saved_data = []
    for item in tqdm(data):
        try:
            message = item["messages"]
            completion = client.chat.completions.create(
                model=args.model,
                messages=message,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                top_p=args.top_p        
            )
            response = {
                "messages": message + [
                    {
                        "role": "assistant",
                        "content": completion.choices[0].message.content
                    }
                ],
                "metadata": item["metadata"]
            }
            saved_data.append(response)
        except Exception as e:
            print(f"Error: {e}")
            continue

    if args.num_trials > 1:
        save_dataset(saved_data, output_files[i], convert_to_jsonl=True)
        print(f"Saved to {output_files[i]}")
    else:
        save_dataset(saved_data, output_file, convert_to_jsonl=True)
        print(f"Saved to {output_file}")
