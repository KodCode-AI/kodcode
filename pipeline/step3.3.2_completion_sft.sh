#!/bin/bash

input_file=${1}
num_trials=${2:-3}
llm=${3:-open_model}
open_model_path=${4:-"deepseek-ai/DeepSeek-R1"}
engine=${5:-"together"}
max_tokens=${6:-16384}
api_key=${7:-${TOGETHER_API_KEY}}

if [ "$engine" == "together" ] && [ -z "$api_key" ]; then
    echo "Error: API key is required if using together engine."
    echo "Please set the API key in the environment variable TOGETHER_API_KEY. Do not start with Bearer, just the key."
    exit 1
fi

if [ -z "$input_file" ]; then
    echo "Error: Input file is required."
    exit 1
fi

if [ "$llm" == "gpt" ]; then
    python completion_gpt.py --input_file ${input_file}
elif [ "$llm" == "open_model" ]; then
    if [ "$engine" == "vllm" ] || [ "$engine" == "hf" ]; then
        python completion_open_model.py --input_file ${input_file} --model_path ${open_model_path} --engine ${engine} --max_tokens ${max_tokens} --num_trials ${num_trials}
    elif [ "$engine" == "together" ]; then
        python completion_open_model.py --input_file ${input_file} --model_path ${open_model_path} --engine ${engine} --max_tokens ${max_tokens} --num_trials ${num_trials} --api_key ${api_key} --batch_size 50
    else
        echo "Error: Invalid engine. Please use 'vllm', 'hf', or 'together'."
        exit 1
    fi
else
    echo "Error: Invalid llm. Please use 'gpt' or 'open_model'."
    exit 1
fi