## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown Python code format within the specified sections below. Ensure your code is within code blocks. For the tests, use pytest style by defining individual test functions (without classes) and using assert statements. 

<|Solution Begin|>
[Solution Code in Python]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in Python]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```python
def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b
```
<|Solution End|>

<|Test Begin|>
```python
from solution import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_sign_numbers():
    assert add(-1, 3) == 2
```
<|Test End|>

## Question:
