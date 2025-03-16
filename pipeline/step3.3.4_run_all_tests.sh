#!/bin/bash

test_folder=${1:-""}

if [ -z "$test_folder" ]; then
    echo "Error: test_folder is required."
    exit 1
fi

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

        # Create a lock file to avoid directory concurrency issues
        LOCK_FILE=".test_running.lock"
        if ! mkdir "$LOCK_FILE" 2>/dev/null; then
            echo "Another process is already running tests in ${inner_dir}. Skipping."
            popd > /dev/null
            return
        fi
        
        bash "run_test.sh"
        
        # Remove the lock directory when done
        rmdir "$LOCK_FILE" 2>/dev/null

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

# Find all test directories
test_dirs=$(find "$test_folder" -mindepth 2 -maxdepth 2 -type d | sort)

# count the number of test_dirs
num_tests=$(echo "$test_dirs" | wc -l)
echo "Number of test directories: $num_tests"
echo -n "Do you want to proceed with running $num_tests tests? [y/N] "
read answer
if [[ ! "$answer" =~ ^[Yy]$ ]]; then
    echo "Aborting..."
    exit 1
fi

# Process test directories in batches of 5000
echo "Processing tests in batches..."
total_tests=$(echo "$test_dirs" | wc -l)
batch_size=5000
num_batches=$(( (total_tests + batch_size - 1) / batch_size ))
start_time=$(date +%s)

for ((batch_num=1; batch_num<=num_batches; batch_num++)); do
    batch_start=$(date +%s)
    echo "Starting batch $batch_num of $num_batches..."
    
    # Calculate the start and end index of the current batch
    start_idx=$(( (batch_num-1) * batch_size + 1 ))
    end_idx=$((batch_num * batch_size))
    if [ $end_idx -gt $total_tests ]; then
        end_idx=$total_tests
    fi
    
    # Extract the test directories for the current batch
    current_batch=$(echo "$test_dirs" | sed -n "${start_idx},${end_idx}p")
    
    # Run tests in parallel for the current batch
    parallel --progress -j $(($(nproc) / 2)) run_test ::: $current_batch
    
    batch_end=$(date +%s)
    batch_duration=$((batch_end - batch_start))
    echo "Completed batch $batch_num in $(date -u -d @${batch_duration} +"%H:%M:%S")."
    
    # Estimate remaining time
    if [ $batch_num -eq 1 ]; then
        avg_batch_time=$batch_duration
    else
        avg_batch_time=$(( (avg_batch_time * (batch_num - 1) + batch_duration) / batch_num ))
    fi
    
    remaining_batches=$((num_batches - batch_num))
    est_remaining_time=$((remaining_batches * avg_batch_time))
    echo "Estimated remaining time: $(date -u -d @${est_remaining_time} +"%H:%M:%S") (${remaining_batches} batches left)"
    
    sleep 5
done

total_time=$(($(date +%s) - start_time))
echo "Test execution completed in $(date -u -d @${total_time} +"%H:%M:%S")."