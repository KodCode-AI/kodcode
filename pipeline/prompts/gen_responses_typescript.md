## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown TypeScript code format within the specified sections below. Ensure your code is within code blocks. Use Jest for the tests.

<|Solution Begin|>
[Solution Code in TypeScript]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in TypeScript using Jest]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```typescript
// Returns the sum of a and b.
function add(a: number, b: number): number {
    return a + b;
}
```
<|Solution End|>

<|Test Begin|>
```typescript
describe('add function', () => {
    test('should add positive numbers', () => {
        expect(add(2, 3)).toBe(5);
        expect(add(10, 15)).toBe(25);
    });
    
    test('should handle zero', () => {
        expect(add(0, 5)).toBe(5);
        expect(add(5, 0)).toBe(5);
        expect(add(0, 0)).toBe(0);
    });
    
    test('should add negative numbers', () => {
        expect(add(-1, -1)).toBe(-2);
        expect(add(-5, -10)).toBe(-15);
    });
    
    test('should handle mixed sign numbers', () => {
        expect(add(-1, 3)).toBe(2);
        expect(add(10, -5)).toBe(5);
        expect(add(-10, 5)).toBe(-5);
    });
});
```
<|Test End|>

## Question:
