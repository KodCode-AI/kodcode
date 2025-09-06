## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown Go code format within the specified sections below. Ensure your code is within code blocks. For the tests, use Go Test style. 

<|Solution Begin|>
[Solution Code in Go]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in Go]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```go
package solution

func Add(a, b int) int {
    return a + b
}
```
<|Solution End|>

<|Test Begin|>
```go
package solution

import "testing"

func TestAddPositiveNumbers(t *testing.T) {
	if got := Add(2, 3); got != 5 {
		t.Errorf("Add(2, 3) = %d; want 5", got)
	}
}

func TestAddWithZero(t *testing.T) {
	if got := Add(0, 5); got != 5 {
		t.Errorf("Add(0, 5) = %d; want 5", got)
	}
	if got := Add(5, 0); got != 5 {
		t.Errorf("Add(5, 0) = %d; want 5", got)
	}
}

func TestAddNegativeNumbers(t *testing.T) {
	if got := Add(-1, -1); got != -2 {
		t.Errorf("Add(-1, -1) = %d; want -2", got)
	}
}

func TestAddMixedSignNumbers(t *testing.T) {
	if got := Add(-1, 3); got != 2 {
		t.Errorf("Add(-1, 3) = %d; want 2", got)
	}
}
```
<|Test End|>

## Question:
