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

# Find all test directories and write them to a temporary file with NUL separators
temp_file=$(mktemp)
find "$test_folder" -mindepth 2 -maxdepth 2 -type d -print0 | sort -z > "$temp_file"

# count the number of test_dirs
num_tests=$(tr -cd '\0' < "$temp_file" | wc -c)
echo "Number of test directories: $num_tests"
# echo -n "Do you want to proceed with running $num_tests tests? [y/N] "
# read answer
# if [[ ! "$answer" =~ ^[Yy]$ ]]; then
#     echo "Aborting..."
#     exit 1
# fi

# Process test directories in batches of 5000
echo "Processing tests in batches..."
batch_size=5000
num_batches=$(( (num_tests + batch_size - 1) / batch_size ))
start_time=$(date +%s)

for ((batch_num=1; batch_num<=num_batches; batch_num++)); do
    batch_start=$(date +%s)
    echo "Starting batch $batch_num of $num_batches..."
    
    # Create a temporary file for the current batch
    batch_file=$(mktemp)
    
    # Calculate the start and end index of the current batch
    start_idx=$(( (batch_num-1) * batch_size ))
    count=$batch_size
    if [ $start_idx -gt $num_tests ]; then
        continue
    fi
    if [ $((start_idx + count)) -gt $num_tests ]; then
        count=$((num_tests - start_idx))
    fi
    
    # Extract the test directories for the current batch using null delimiter
    head -z -n $((start_idx + count)) "$temp_file" | tail -z -n $count > "$batch_file"
    
    # Run tests in parallel for the current batch using null delimiter
    parallel --progress -j $(nproc) --null run_test :::: "$batch_file"
    
    # Clean up temporary batch file
    rm -f "$batch_file"
    
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

# Clean up temporary file
rm -f "$temp_file"

total_time=$(($(date +%s) - start_time))
echo "Test execution completed in $(date -u -d @${total_time} +"%H:%M:%S")."