#!/bin/bash

input_file=${1:-"../data_step1/CodeGen_leetcode_10_1741075944/CodeGen_seed_leetcode_10_1741075944.jsonl"}

python gpt_api_call.py --input_file ${input_file}
