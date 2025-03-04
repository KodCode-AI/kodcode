#!/bin/bash

input_file=${1:-"../data_step1/CodeGen_leetcode_10_1741075944/CodeGen_instruction_leetcode_10_1741075944_sanitized_prepared.jsonl"}

python gpt_api_call.py --input_file ${input_file}
