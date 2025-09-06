## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown C++ code format within the specified sections below. Ensure your code is within code blocks. Use assertion for the tests.

<|Solution Begin|>
[Solution Code in C++]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in C++]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```cpp
#include<assert.h>
#include<bits/stdc++.h>

// Returns the sum of a and b.
int add(int a, int b) {
    return a + b;
}
```
<|Solution End|>

<|Test Begin|>
```cpp
#include<assert.h>
#include<bits/stdc++.h>
#include "solution.cpp"

int main() {
    auto candidate = add;
    
    // Test positive numbers
    assert(candidate(2, 3) == 5);
    assert(candidate(10, 15) == 25);
    
    // Test with zero
    assert(candidate(0, 5) == 5);
    assert(candidate(5, 0) == 5);
    assert(candidate(0, 0) == 0);
    
    // Test negative numbers
    assert(candidate(-1, -1) == -2);
    assert(candidate(-5, -10) == -15);
    
    // Test mixed sign numbers
    assert(candidate(-1, 3) == 2);
    assert(candidate(10, -5) == 5);
    assert(candidate(-10, 5) == -5);
}
```
<|Test End|>

## Question:
