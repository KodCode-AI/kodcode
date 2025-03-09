#!/bin/bash

# Define the log and result file paths
LOG_FILE="test_log.log"
RESULT_FILE="test_result.txt"
TIME_LIMIT=30  # Timeout limit in seconds

# Function to clean up temporary files
cleanup() {
    rm -rf __pycache__
    rm -rf .pytest_cache
    rm -f .coverage
}

# Ensure cleanup happens even if the script exits early
trap cleanup EXIT

# Run pytest with a timeout limit, redirecting output to the log file
timeout $TIME_LIMIT pytest --cov=solution --cov-report term > $LOG_FILE 2>&1
PYTEST_STATUS=$?

# Check the exit status of pytest
if [ $PYTEST_STATUS -eq 0 ]; then
    echo "Tests completed successfully."
    echo "Pass" > $RESULT_FILE
    EXIT_CODE=0
elif [ $PYTEST_STATUS -eq 124 ]; then
    # 124 is the exit code for a timeout
    echo "Tests timed out."
    echo "Fail - Timed Out" > $RESULT_FILE
    EXIT_CODE=1
else
    echo "Some tests failed. Check the output for details."
    echo "Fail" > $RESULT_FILE
    EXIT_CODE=1
fi

# Extract the coverage percentage from the log file and append it to the result file
COVERAGE=$(grep 'TOTAL' $LOG_FILE | awk '{print $4}')
echo "Coverage: $COVERAGE" >> $RESULT_FILE

exit $EXIT_CODE

# Extract the coverage percentage from the log file and append it to the result file
COVERAGE=$(grep 'TOTAL' $LOG_FILE | awk '{print $4}')
echo "Coverage: $COVERAGE" >> $RESULT_FILE