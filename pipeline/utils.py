import json
import requests
import uuid
from time import sleep
import ast
import inspect
import types
import os
import re

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

# Safe checkpoint saving with backup
def safe_save_checkpoint(data, checkpoint_file, convert_to_jsonl=False):
    """
    Safely save checkpoint data with backup mechanism:
    1. Rename existing checkpoint to _old
    2. Save new checkpoint
    3. Remove old backup
    
    Args:
        data: Data to save
        checkpoint_file: Path to checkpoint file
        convert_to_jsonl: Whether to save as JSONL format
    """
    old_checkpoint = f"{checkpoint_file}_old"
    
    try:
        # Step 1: Backup existing checkpoint if it exists
        if os.path.exists(checkpoint_file):
            if os.path.exists(old_checkpoint):
                os.remove(old_checkpoint)  # Remove any existing old backup
            os.rename(checkpoint_file, old_checkpoint)
            print(f"📦 Backed up existing checkpoint to {old_checkpoint}")
        
        # Step 2: Save new checkpoint
        save_dataset(data, checkpoint_file, convert_to_jsonl=convert_to_jsonl)
        print(f"💾 Saved new checkpoint to {checkpoint_file}")
        
        # Step 3: Clean up old backup
        if os.path.exists(old_checkpoint):
            os.remove(old_checkpoint)
            print(f"🗑️  Removed old backup {old_checkpoint}")
            
    except Exception as e:
        print(f"❌ Error during checkpoint save: {str(e)}")
        
        # Try to restore from backup if new save failed
        if os.path.exists(old_checkpoint) and not os.path.exists(checkpoint_file):
            try:
                os.rename(old_checkpoint, checkpoint_file)
                print(f"🔄 Restored checkpoint from backup")
            except Exception as restore_error:
                print(f"❌ Failed to restore from backup: {str(restore_error)}")
        
        raise e  # Re-raise the original error

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
    elif "diversify" in mode.lower():
        return "Diversify"
    else:
        raise ValueError(f"Unknown mode: {mode}")

def get_model_short_name(model_path):
    # Remove org name if present (e.g., "Qwen/Qwen3-32B" -> "Qwen3-32B")
    if "/" in model_path:
        return model_path.split("/")[-1]
    return model_path

# Get model abbreviation from model_configs.json
def get_model_abbreviation(model_path, config_file="model_configs.json"):
    """
    Get model abbreviation from model_configs.json
    
    Args:
        model_path: Full model path (e.g., "Qwen/Qwen3-32B")
        config_file: Path to model configs file
        
    Returns:
        str: Model abbreviation (e.g., "q332b")
    """
    try:
        with open(config_file, 'r') as f:
            model_configs = json.load(f)
        
        if model_path in model_configs:
            return model_configs[model_path]["abbreviation"]
        else:
            print(f"⚠️  Model {model_path} not found in {config_file}, falling back to get_model_short_name")
            return get_model_short_name(model_path)
    except FileNotFoundError:
        print(f"⚠️  {config_file} not found, falling back to get_model_short_name")
        return get_model_short_name(model_path)
    except Exception as e:
        print(f"⚠️  Error reading {config_file}: {str(e)}, falling back to get_model_short_name")
        return get_model_short_name(model_path)


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

def clean_unusual_line_terminators(text):
    """
    Remove unusual line terminator characters like Line Separator (U+2028) 
    and Paragraph Separator (U+2029) that can cause issues.
    """
    if isinstance(text, str):
        # Remove Line Separator (U+2028) and Paragraph Separator (U+2029)
        text = text.replace('\u2028', ' ').replace('\u2029', ' ')
        # Also clean other problematic Unicode characters
        text = text.replace('\u0085', ' ')  # Next Line (NEL)
        text = text.replace('\u000B', ' ')  # Vertical Tab
        text = text.replace('\u000C', ' ')  # Form Feed
    return text

def clean_json_object(obj):
    """
    Recursively clean unusual line terminators from a JSON object.
    """
    if isinstance(obj, str):
        return clean_unusual_line_terminators(obj)
    elif isinstance(obj, dict):
        return {key: clean_json_object(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [clean_json_object(item) for item in obj]
    else:
        return obj

def clean_html_comments(text):
    """
    Remove HTML comments from text content.
    Removes patterns like <!-- followed by any content (non-greedy) and -->
    """
    if not text:
        return text
    
    # Remove HTML comments using regex
    # This pattern matches <!-- followed by any content (non-greedy) and -->
    cleaned_text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # Clean up any extra whitespace that might be left
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

################
# Data Preview
################

def create_preview_json(input_file, output_file, num_entries=5):
    """
    Create a preview JSON file with the first N entries from a JSONL file.
    """
    preview_data = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= num_entries:
                    break
                preview_data.append(json.loads(line))
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(preview_data, f, ensure_ascii=False, indent=2)
        
        print(f"Preview with {len(preview_data)} entries saved to {output_file}")
    except Exception as e:
        print(f"Error creating preview for {input_file}: {e}")