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
    parser.add_argument("--max_tokens", type=int, default=4096, help="Max tokens for the API call.")
    parser.add_argument("--top_p", type=float, default=1.0, help="Top p for the API call.")
    return parser.parse_args()

args = get_args()
args.output_file = args.input_file.replace(".jsonl", "_results.jsonl")

data = load_dataset_from_file(args.input_file)

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

save_dataset(saved_data, args.output_file, convert_to_jsonl=True)
print(f"Saved to {args.output_file}")