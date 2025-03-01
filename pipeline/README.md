# KodCode Pipeline

Here, we provide our pipeline for generating KodCode dataset.

## Step 1: Generate Questions

### Step 1.1: Generate Questions from Code

To generate synthetic questions, we first need to put seed questions/snippets/docs in the [`../seeds`](../seeds) folder.

Then, we can run the following command to generate questions. Available modes are `leetcode`, `algorithm`, `data_structure`, `package`, `apps`, `codeforces`, `code_contests`, `taco`, and `docs`.

```bash
python step1.1_gen_questions.py --total_prompts [total_prompts] --mode [mode]
```

### Step 1.2: Obtain GPT-4o Completion

We then call the GPT-4o API to generate instructions for each question.

### Step 1.3: Filter Out Questions and Perform Deduplication

To do this step, simply run the following command.

```bash
python step1.3_proccess_and_sanitize.py --input_file [file_name]
```

## Step 2: Generate Solutions and Tests

### Step 2.1: Obtain GPT-4o Completion

After you get the filtered instructions, you can run the following command to generate solutions and tests.

```bash
bash step2.1_gpt_completion.sh [file_name]
```

### Step 2.2: Process Responses and Generate Unit Tests

This step will generate unit tests for each solution. The input folder contains trials of solutions and tests. In our experiments, we use 10 trials for each solution.

```bash
python step2.2_gen_unit_tests.py --input_folder [folder_name]
```

A folder starts with `unit_test_` will be generated, which contains the unit tests for each solution.

### Step 2.3: Run All Tests

This step will run all the tests and generate the results.

```bash
bash step2.3_run_all_tests.sh [unit_test_folder_name]
```

### Step 2.4: Generate Verified Triplets

This step will generate verified triplets for each solution.

```bash
python step2.4_gen_verified_triplets.py --unit_test_folder [unit_test_folder_name]
```

After this step, you will get the verified question-solution-test triplets.