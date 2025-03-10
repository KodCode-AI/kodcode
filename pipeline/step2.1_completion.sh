#!/bin/bash

input_file=${1}
num_trials=${2:-1}
llm=${3:-open_model}
open_model_path=${4:-"Qwen/Qwen2.5-7B-Instruct"}

if [ -z "$input_file" ]; then
    echo "Error: Input file is required."
    exit 1
fi

if [ "$llm" == "gpt" ]; then
    python completion_gpt.py --input_file ${input_file} --num_trials ${num_trials}
elif [ "$llm" == "open_model" ]; then
    python completion_open_model.py --input_file ${input_file} --num_trials ${num_trials} --model_path ${open_model_path}
else
    echo "Error: Invalid llm. Please use 'gpt' or 'open_model'."
    exit 1
fi
