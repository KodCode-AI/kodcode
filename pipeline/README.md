# KodCode Pipeline

Here, we provide our pipeline for generating KodCode dataset.

## Step 1: Coding Question Synthesis

### Step 1.1: Generate Questions from Seeds

To generate synthetic questions, we first need to put seed questions/snippets/docs in the [`../seeds`](../seeds) folder.

Then, we can run the following command to generate questions. Available modes are `leetcode`, `algorithm`, `data_structure`, `package`, `apps`, `codeforces`, `code_contests`, `taco`, `docs`, and `prefill`.

```bash
python step1.1_gen_questions.py --total_prompts [total_prompts] --mode [mode]
```

**Example:** We take `leetcode` as an example and generate 100 questions:

```bash
python step1.1_gen_questions.py --total_prompts 100 --mode leetcode
```

You can now find the generated questions in the `../demo/KodCode_leetcode_100_1741214688` folder, where `leetcode` is the mode, `100` is the number of questions generated, and `1741214688` is the timestamp to distinguish different runs.

The file name in this example is `KodCode_seeds2questions_leetcode_100_1741214688.jsonl`. `seeds2questions` stands for this file is used for generating questions from seeds.

### Step 1.2: Obtain Completion

We then call LLMs to generate questions from the seeds. You can choose to use either GPT-4o (set llm as `gpt`) or open models (set llm as `open_model`). Current we support `vllm`, `huggingface` and `together` engines for open models.

```bash
bash step1.2_completion.sh [input_file] [llm] [model_name(optional)]
```

**Example:** We use open models to generate questions from the seeds:

```bash
bash step1.2_completion.sh ../demo/KodCode_leetcode_100_1741214688/KodCode_seeds2questions_leetcode_100_1741214688.jsonl open_model
```

You can now find the output file as `KodCode_seeds2questions_leetcode_100_1741214688_results.jsonl` in the input folder. Note that the file name is the same as the input file, but with `_results` appended to the end, indicating that the file contains the completion results of the LLM generation.

### Step 1.3: Filter Out Questions and Perform Deduplication

To do this step, simply run the following command.

```bash
python step1.3_proccess_and_sanitize.py --input_file [file_name]
```

**Example:** We filter out the questions and perform deduplication we generated from Step 1.2.

```bash
python step1.3_proccess_and_sanitize.py --input_file ../demo/KodCode_leetcode_100_1741214688/KodCode_seeds2questions_leetcode_100_1741214688_results.jsonl
```

You can now find the output file as `KodCode_questions2sv_leetcode_100_1741214688_sanitized_prepared.jsonl` in the input folder. We use `_prepared` to indicate that this file is ready for LLM completion. `questions2sv` stands for this file is used for generating solutions and testsfrom questions.

## Step 2: Generate Solutions and Tests

### Step 2.1: Obtain GPT-4o Completion

After you get the filtered instructions, you can run the following command to generate solutions and tests. Num_trials is the number of attempts for each question.

```bash
bash step2.1_completion.sh [file_name] [num_trials] [llm] [model_name(optional)]
```

**Example:** We use GPT-4o to generate solutions and tests. We set num_trials as 3.

```bash
bash step2.1_completion.sh ../demo/KodCode_leetcode_100_1741214688/KodCode_questions2sv_leetcode_100_1741214688_sanitized_prepared.jsonl 3 gpt
```

You can now find three new files `KodCode_questions2sv_leetcode_100_1741214688_sanitized_prepared_results{0,1,2}.jsonl` in the input folder.

### Step 2.2: Process Responses and Generate Unit Tests

This step will generate unit tests for each solution. The input folder contains trials of solutions and tests. It will automatically find all files from Step 2.1.

```bash
python step2.2_gen_unit_tests.py --input_folder [folder_name]
```

A folder starts with `unit_test_` will be generated, which contains the executable unit tests for each solution.

**Example:** We use the folder generated from Step 2.1.

```bash
python step2.2_gen_unit_tests.py --input_folder ../demo/KodCode_leetcode_100_1741214688
```

### Step 2.3: Run All Tests

This step will run all the tests and generate the results. By default, we use `parallel` to run the tests.

```bash
bash step2.3_run_all_tests.sh [unit_test_folder_name]
```

**Example:** We use the unit testfolder generated from Step 2.2.

```bash
bash step2.3_run_all_tests.sh ../demo/KodCode_leetcode_100_1741214688/self_verification_KodCode_leetcode_100_1741214688
```

### Step 2.4: Generate Verified Triplets

This step will generate verified triplets for each solution.

```bash
python step2.4_gen_verified_triplets.py --unit_test_folder [unit_test_folder_name]
```

**Example:** We use the unit test folder generated from Step 2.3.

```bash
python step2.4_gen_verified_triplets.py --unit_test_folder ../demo/KodCode_leetcode_100_1741214688/self_verification_KodCode_leetcode_100_1741214688
```

After this step, you will get the verified question-solution-test triplets. In this example, we will get the file `Verified_KodCode_leetcode_100_1741214688.json` in `demo` folder.
