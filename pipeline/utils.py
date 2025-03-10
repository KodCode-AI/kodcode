import json
import requests
import uuid
from time import sleep

# File I/O utilities
def load_jsonl_to_list(jsonl_file_path):
    data_list = []
    with open(jsonl_file_path, 'r') as file:
        for line in file:
            json_obj = json.loads(line)
            data_list.append(json_obj)
    return data_list

# Load dataset
def load_dataset_from_file(filename):
    #if the file is json
    if filename.endswith('.json'):
        with open(filename, 'r') as file:
            return json.load(file)
    elif filename.endswith('.jsonl'):
        return load_jsonl_to_list(filename)
    else:
        raise ValueError("Invalid file format. Please provide a .json or .jsonl file.")

# Save dataset
def save_dataset(data, filename, convert_to_jsonl=False):
    if convert_to_jsonl:
        with open(filename, 'w') as file:
            for obj in data:
                file.write(json.dumps(obj) + '\n')
    else:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)


# Function to make a single API request with exponential back-off
def make_api_request_with_retry(message, api_params, api_endpoint, api_headers, max_retries=5):
    payload = api_params.copy()
    payload['messages'] = message

    for attempt in range(max_retries):
        try:
            response = requests.post(api_endpoint, json=payload, headers=api_headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()['choices'][0]['message']['content']
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            sleep(2 ** attempt)  # Exponential back-off
    
    print("All retry attempts failed.")
    return None