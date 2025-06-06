# KodCode Pipeline

Here, we provide our pipeline for generating KodCode dataset. Please ensure you are in the `pipeline` folder when running the commands.

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
python step1.3_process_and_sanitize.py --input_file [file_name]
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

Option 1: local environment

```bash
bash step2.3_run_all_tests.sh [unit_test_folder_name]
```

Option 2: docker environment (recommended)

```bash
docker run --gpus all -it --rm \
  --entrypoint bash \
  -v $(pwd)/..:/app \
  -w /app/pipeline \
  zcxu/kodcode-test-environment:python3.10-cuda12.4-v0.1 \
  -c "bash step2.3_run_all_tests.sh [unit_test_folder_name]"
```

**Example:** We use the unit testfolder generated from Step 2.2 and run all tests using local environment.

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
python step2.4_gen_verified_triplets.py --test_folder ../demo/KodCode_leetcode_100_1741214688/self_verification_KodCode_leetcode_100_1741214688
```

After this step, you will get the verified question-solution-test triplets. In this example, we will get the file `Verified_KodCode_leetcode_100_1741214688.json` in `demo` folder.

## Step 3: Post-training Data Synthesis

### Step 3.1: Style Converter

#### Step 3.1.1: Convert Instruct to Complete

To convert the style of the generated data from instruct to complete, we can run the following command. This will generate a new folder in the `../demo` folder, and the name of the folder is `Complete_<input_file_name>`. 

```bash
python step3.1.1_style_converter.py --input_file [file_name]
```

**Example:** We use the file generated from Step 2.4.

```bash
python step3.1.1_style_converter.py --input_file ../demo/Verified_KodCode_leetcode_100_1741214688.json
```

You can now find the output file as `Verified_KodCode_leetcode_100_1741214688_i2c_prepared.json` in the `../demo/Complete_Verified_KodCode_leetcode_100_1741214688` folder.

#### Step 3.1.2: Obtain GPT-4o Completion

We can now use GPT-4o to generate the completion questions.

```bash
bash step3.1.2_completion.sh [file_name] [llm]
```

**Example:** We use GPT-4o to generate the completion questions.

```bash
bash step3.1.2_completion.sh ../demo/Complete_Verified_KodCode_leetcode_100_1741214688/Complete_KodCode_leetcode_100_1741214688_i2c_prepared.json gpt
```

You can now find the output file as `Verified_KodCode_leetcode_100_1741214688_i2c_prepared_results.jsonl` in the `../demo/Complete_Verified_KodCode_leetcode_100_1741214688` folder.

#### Step 3.1.3: Organize the Data

This step will organize the data into the format of the post-training data by extracting the completion from the GPT-4o completion results.

```bash
python step3.1.3_gen_complete_triplets.py --input_file [file_name]
```

**Example:** We use the file generated from Step 3.1.2.

```bash
python step3.1.3_gen_complete_triplets.py --input_file ../demo/Complete_Verified_KodCode_leetcode_100_1741214688/Complete_KodCode_leetcode_100_1741214688_i2c_prepared_results.jsonl
```

You can now find the output file as `Verified_KodCode_leetcode_100_1741214688_Complete.json` in the `../demo/Complete_Verified_KodCode_leetcode_100_1741214688` folder.

### Step 3.2: Combine Instruct and Complete Triplets

This step will combine the instruct and complete triplets into a single file. Note that the `kodcode_exp_name` is the name of the experiment, which is used to distinguish different runs.

```bash
python step3.2_combine_kodcode.py --kodcode_exp_name [kodcode_exp_name]
```

**Example:** We use the files generated from Step 2.4 and Step 3.1.3. Here, the `kodcode_exp_name` is `KodCode_leetcode_100_1741214688`.

```bash
python step3.2_combine_kodcode.py --kodcode_exp_name KodCode_leetcode_100_1741214688
```

You can now find the output file as `KodCode_leetcode_100_1741214688.json` in the `../demo` folder.

### Step 3.3: SFT Data Generation

#### Step 3.3.1: Process the Data

Now we are generating the SFT data. We first need to process the data for the completion pipeline. This step will generate a new folder in the `../demo` folder, and the name of the folder is `SFT_<input_file_name>`. 

```bash
python step3.3.1_proccess_sft.py --input_file [file_name]
```

**Example:** We use the file generated from Step 3.2.

```bash
python step3.3.1_proccess_sft.py --input_file ../demo/KodCode_leetcode_100_1741214688.json
```

You can now find the output file as `SFT_KodCode_leetcode_100_1741214688/KodCode_leetcode_100_1741214688_prepared.jsonl` in the `../demo` folder.

#### Step 3.3.2: Generate SFT Data

This step will generate the SFT data. Since we are using DeepSeek-R1 and together engine, we need to set the together API Key in the environment variable `TOGETHER_API_KEY`. Do not start with Bearer, just the key.

```bash
export TOGETHER_API_KEY=[your_together_api_key]
bash step3.3.2_completion_sft.sh [file_name] [num_trials] [llm] [model_name(optional)] [engine(optional)] [max_tokens(optional)] 
```

**Example:** The following command will generate the SFT data using DeepSeek-R1 with 3 trials.

```bash
bash step3.3.2_completion_sft.sh ../demo/SFT_KodCode_leetcode_100_1741214688/SFT_KodCode_leetcode_100_1741214688_prepared.jsonl 3 open_model deepseek-ai/DeepSeek-R1 together 16384
```

You can now find three files as `SFT_KodCode_leetcode_100_1741214688_results{0,1,2}.jsonl` in the `../demo/SFT_KodCode_leetcode_100_1741214688` folder, representing the results of the three trials.

#### Step 3.3.3: Generate Unit Tests for SFT Data

This step will generate the unit tests for the SFT data.

```bash
python step3.3.3_gen_unit_tests_sft.py --input_folder [folder_name]
```

**Example:** We use the folder contains the SFT data generated from Step 3.3.2 with 3 trials. Since we are using DeepSeek-R1, we set the `model_nickname` as `r1` for distinguishing in test folder names.

```bash
python step3.3.3_gen_unit_tests_sft.py --input_folder ../demo/SFT_KodCode_leetcode_100_1741214688 --model_nickname r1
```

You can now find the unit test folder as `cross_verification_KodCode_leetcode_100_1741214688` in the `../demo/SFT_KodCode_leetcode_100_1741214688` folder.

#### Step 3.3.4: Run All Tests for SFT Data

This step will run all the tests for the SFT data.

```bash
bash step3.3.4_run_all_tests_sft.sh [unit_test_folder_name]
```

**Example:** We use the unit test folder generated from Step 3.3.3.

```bash
bash step3.3.4_run_all_tests_sft.sh ../demo/SFT_KodCode_leetcode_100_1741214688/cross_verification_KodCode_leetcode_100_1741214688
```

#### Step 3.3.5: Generate SFT Data with Correctness Labels

This step will generate the SFT data with correctness labels.

```bash
python step3.3.5_gen_sft_datasets.py --input_folder [folder_name]
```

**Example:** We use the unit test folder executed in Step 3.3.4.

```bash
python step3.3.5_gen_sft_datasets.py --input_folder ../demo/SFT_KodCode_leetcode_100_1741214688/cross_verification_KodCode_leetcode_100_1741214688
```

The final output folder should now appears as `SFT_KodCode_leetcode_100_1741214688.json` in the `../demo` folder. For each question, there is a correctness label named as `r1_correctness`. If the response is correct, the label is `True`, otherwise it is `False`.
