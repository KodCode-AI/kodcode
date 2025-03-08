import re

def input_classification(input):
    user_message = f'''
# Instruction

Please label the task tags for the user query.

## User Query
```
{input}
```

## Tagging the user input
Please label the task tags for the user query. You will need to analyze the user query and select the most relevant task tag from the list below.

all_task_tags = [
    "Debugging",  # Users ask for help with debugging code. The user should provide the code and error message.
    "Code Review",  # Users ask for help with reviewing code. The user should provide the code.
    "Code Refactoring",  # Users ask for help with refactoring code to improve its structure.
    "Code Optimization",  # Users ask for help with improving code performance or efficiency.
    "Function Generation",  # Users ask for help with creating new functions based on requirements.
    "Class Design",  # Users ask for help with designing classes and object-oriented structures.
    "Algorithm Implementation",  # Users ask for help with implementing specific algorithms or data structures.
    "API Integration",  # Users ask for help with integrating third-party APIs or services.
    "Database Operations",  # Users ask for help with database queries, schema design, or operations.
    "Testing",  # Users ask for help with unit tests, integration tests, or test strategies.
    "Security",  # Users ask for help with security-related implementations or best practices.
    "Error Handling",  # Users ask for help with implementing error handling and validation.
    "Concurrency",  # Users ask for help with multi-threading, async programming, or parallel processing.
    "UI/UX Implementation",  # Users ask for help with frontend implementations or user interface code.
    "DevOps",  # Users ask for help with deployment, CI/CD, or infrastructure code.
    "Documentation",  # Users ask for help with code documentation or technical writing.
    "Dependency Management",  # Users ask for help with package management or dependency issues.
    "Code Migration",  # Users ask for help with migrating code between languages or frameworks.
    "Performance Profiling",  # Users ask for help with identifying and resolving performance bottlenecks.
    "Others"  # Any queries that do not fit into the above categories.
]

## Output Format:
Note that you can only select a single primary tag. Other applicable tags can be added to the list of other tags.
Now, please output your tags below in a json format by filling in the placeholders in <...>:
```
{{ 
    "primary_tag": "<primary tag>",
    "other_tags": ["<tag 1>", "<tag 2>", ... ]
}}
```
'''
    return user_message

def input_quality_rating(input):
    user_message = f'''
# Instruction

You need to rate the quality of the code-related query based on its clarity, specificity, and completeness.

The rating scale is as follows:

- very poor: The query lacks critical code context (e.g., no code samples, error messages, or specific requirements). The problem description is vague or incoherent.
- poor: The query provides incomplete code context or unclear requirements. Important details like programming language, error messages, or expected behavior are missing.
- average: The query includes basic code context and requirements but may need clarification on specific behaviors, edge cases, or implementation details.
- good: The query provides clear code samples, specific requirements, and sufficient context (e.g., language version, environment, expected behavior). Minor details might be missing.
- excellent: The query is comprehensive with complete code examples, clear requirements, relevant error messages if applicable, expected behavior, and implementation constraints. All necessary context is provided for solving the problem.

If the query is not related to code, please rate it as `very poor`. If the query is short but clearly demonstrates the user's intent, please rate it as `good`.

If the query only contains code with no specific instructions, please rate it as `very poor`.

If the query explicitly asks to use programming language other than Python, please rate it as `very poor`.

## User Query
```
{input}
```

## Output Format
Given the user query, you first need to give an assesement, highlighting the strengths and/or weaknesses of the user query.
Then, you need to output a rating from very poor to excellent by filling in the placeholders in [...]:
```
{{   
    "explanation": "[...]",
    "input_quality": "[very poor/poor/average/good/excellent]"
}}
```
'''
    return user_message


def input_type(input):
    user_message = f'''
# Instruction

Please determine if the user query can be represented as an Online Judge (OJ) problem.

## User Query
```
{input}
```

## Classification Criteria
Analyze the query and determine if it can be represented as an Online Judge (OJ) problem, typically solved with stdin/stdout processing.

A query is NOT an OJ problem if any of the following conditions are met:
1. It explicitly defines a function signature (e.g., `def sort_array(array):`)
2. It specifies a required function name to implement
3. It asks for a self-contained implementation
4. It requests a specific class or object-oriented implementation
5. It asks for code that integrates with existing systems/frameworks
6. It directly asks for explaining, debugging, or reviewing existing code

If the query is not an OJ problem, please output `false`. **In any other case, please output `true`.**

## Output Format
Please output your determination in JSON format:
```
{{
    "is_oj": "<true/false>",
    "explanation": "<explanation>"
}}
```
'''
    return user_message