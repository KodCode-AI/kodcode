## Task:
Please convert the given coding task to a coding completion task.

## Instruction

I will give you a coding task, and you goal is to convert it to a completion task. For example, if the coding task is "Find the longest common prefix among a list of strings.", the completion should be a task requiring the user to write a function that takes a list of strings as input and returns the longest common prefix as shown in the example below. Please ensure that the completion task contains the function definition, necessary imports, description, and test cases (if applicable). 

I will provide you a coding task, along with a unit test and a solution. You can refer to them for the test cases and the function definition, but do not put the solution in the completion task.

Coding Task: Find the longest common prefix among a list of strings.

Unit Test:
```python
from solution import longest_common_prefix

def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
```

Solution:
```python
def longestCommonPrefix(strs: List[str]) -> str:
    # Sort the list of strings
    strs.sort()
    
    # Only need to compare first and last strings after sorting
    first = strs[0]
    last = strs[-1]
    
    # Find the common prefix between first and last
    i = 0
    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1
    
    return first[:i]
```

Completion Task you should generate:
```python
def longest_common_prefix(strs: List[str]) -> str:
    """ Find the longest common prefix among a list of strings.
    >>> longest_common_prefix(["flower", "flow", "flight"]) "fl"
    >>> longest_common_prefix(["dog", "racecar", "car"]) ""
    """
```

Now, I will give you a coding task, and you goal is to convert it to a completion task.
## Input Information

Coding Task: [Coding Task Placeholder]

Unit Test: 
```python
[Unit Test Placeholder]
```

Solution: 
```python
[Solution Placeholder]
```

## Output Format:
<|Completion Begin|>
[Completion Task in Python]
<|Completion End|>

Please output the completion task strictly in the provided format, without adding any other information.
