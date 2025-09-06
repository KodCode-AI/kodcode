## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown Rust code format within the specified sections below. Ensure your code is within code blocks. Use assertion for the tests.

<|Solution Begin|>
[Solution Code in Rust]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in Rust]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```rust
// Returns the sum of a and b.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```
<|Solution End|>

<|Test Begin|>
```rust
fn main() {
    let candidate = add;
    
    // Test positive numbers
    assert_eq!(candidate(2, 3), 5);
    assert_eq!(candidate(10, 15), 25);
    
    // Test with zero
    assert_eq!(candidate(0, 5), 5);
    assert_eq!(candidate(5, 0), 5);
    assert_eq!(candidate(0, 0), 0);
    
    // Test negative numbers
    assert_eq!(candidate(-1, -1), -2);
    assert_eq!(candidate(-5, -10), -15);
    
    // Test mixed sign numbers
    assert_eq!(candidate(-1, 3), 2);
    assert_eq!(candidate(10, -5), 5);
    assert_eq!(candidate(-10, 5), -5);
    
    println!("All tests passed!");
}
```
<|Test End|>

## Question:
