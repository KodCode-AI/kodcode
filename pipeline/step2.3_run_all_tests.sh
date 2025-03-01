#!/bin/bash

test_folder=${1:-"../unit_test_CodeGen_instruction_50000_combined"}

export test_folder

# Function to run individual tests
run_test() {
    inner_dir="$1"
    if [ -f "${inner_dir%/}/run_test.sh" ]; then
        pushd "$inner_dir" > /dev/null
        
        # Skip if test results already exist
        if [ -f "test_result.txt" ]; then
            RESULT=$(cat "test_result.txt")
            echo "Results for ${inner_dir}: $RESULT (using existing results)"
            popd > /dev/null
            return
        fi

        bash "run_test.sh"

        if [ -f "test_result.txt" ]; then
            RESULT=$(cat "test_result.txt")
            echo "Results for ${inner_dir}: $RESULT"
        else
            echo "No result file found in ${inner_dir}."
        fi

        popd > /dev/null
    else
        echo "No test script found in ${inner_dir}."
    fi
}

export -f run_test

# Find all inner directories containing run_test.sh and execute them in parallel
find "$test_folder" -type f -name "run_test.sh" -exec dirname {} \; | parallel --progress -j $(nproc) run_test {}

echo "Test execution completed"