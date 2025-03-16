import json
import requests
import uuid
from time import sleep
import ast
import inspect
import types

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

# Function to extract function info from AST
def extract_function_info_from_ast(code_string):
    """
    Extract function information from code string using AST only, without executing the code
    """
    try:
        parsed_ast = ast.parse(code_string)
    except Exception as e:
        print(f"Error: {e}")
        return []
    
    results = []
    try:
        for node in ast.walk(parsed_ast):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                
                # Extract parameters
                args_info = []
                defaults_offset = len(node.args.args) - len(node.args.defaults)

                # Process regular parameters (possibly with default values)
                for i, arg in enumerate(node.args.args):
                    arg_name = arg.arg
                    if i >= defaults_offset:
                        default_value = ast.unparse(node.args.defaults[i - defaults_offset])
                        args_info.append(f"{arg_name}={default_value}")
                    else:
                        args_info.append(arg_name)

                # Process *args
                if node.args.vararg:
                    args_info.append(f"*{node.args.vararg.arg}")

                # Process keyword parameters (possibly with default values)
                for i, arg in enumerate(node.args.kwonlyargs):
                    arg_name = arg.arg
                    if i < len(node.args.kw_defaults) and node.args.kw_defaults[i] is not None:
                        default_value = ast.unparse(node.args.kw_defaults[i])
                        args_info.append(f"{arg_name}={default_value}")
                    else:
                        args_info.append(arg_name)

                # Process **kwargs
                if node.args.kwarg:
                    args_info.append(f"**{node.args.kwarg.arg}")

                # Build signature string
                signature = f"({', '.join(args_info)})"

                # Generate complete function declaration
                function_declaration = f"def {func_name}{signature}:"

                # Get function docstring (if available)
                docstring = ast.get_docstring(node)

                results.append({
                    'function_name': func_name,
                    'parameter_list': signature,
                    'function_declaration': function_declaration,
                    'docstring': docstring,
                })
    except Exception as e:
        print(f"Error: {e}")
        return []

    return results

# Get the mode of the dataset
def get_mode(mode):
    if "prefill" in mode.lower():
        return "Prefill"
    elif "package" in mode.lower():
        return "Package"
    elif "evol" in mode.lower():
        return "Evol"
    elif "codeforces" in mode.lower():
        return "Codeforces"
    elif "leetcode" in mode.lower():
        return "Leetcode"
    elif "apps" in mode.lower():
        return "Apps"
    elif "taco" in mode.lower():
        return "Taco"
    elif "code_contests" in mode.lower():
        return "Code_Contests"
    elif "algorithm" in mode.lower():
        return "Algorithm"
    elif "data_structure" in mode.lower():
        return "Data_Structure"
    elif "docs" in mode.lower():
        return "Docs"
    elif "filter" in mode.lower():
        return "Filter"
    else:
        raise ValueError(f"Unknown mode: {mode}")

# Get the difficulty of the GPT response
def get_gpt_difficulty(pass_sequence):
    pass_percentage = (sum(pass_sequence) / len(pass_sequence)) if pass_sequence else 0
    
    # Determine difficulty based on pass percentage
    if pass_percentage >= 2/3:
        gpt_difficulty = "easy"
    elif pass_percentage < 1/3:
        gpt_difficulty = "hard"
    else:
        gpt_difficulty = "medium"
    return gpt_difficulty

# Get the pass percentage of the GPT response
def get_gpt_pass_percentage(pass_sequence):
    pass_percentage = (sum(pass_sequence) / len(pass_sequence)) if pass_sequence else 0
    
    return round(pass_percentage, 3)