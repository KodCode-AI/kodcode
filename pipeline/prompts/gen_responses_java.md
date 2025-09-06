## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown Java code format within the specified sections below. Ensure your code is within code blocks. For the tests, use JUnit 5 style. 

<|Solution Begin|>
[Solution Code in Java]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in Java]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```java
public class Solution {
    /**
     * Returns the sum of a and b.
     */
    public static int add(int a, int b) {
        return a + b;
    }
}
```
<|Solution End|>

<|Test Begin|>
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SolutionTest {
    
    @Test
    public void testAddPositiveNumbers() {
        assertEquals(5, Solution.add(2, 3));
    }
    
    @Test
    public void testAddWithZero() {
        assertEquals(5, Solution.add(0, 5));
        assertEquals(5, Solution.add(5, 0));
    }
    
    @Test
    public void testAddNegativeNumbers() {
        assertEquals(-2, Solution.add(-1, -1));
    }
    
    @Test
    public void testAddMixedSignNumbers() {
        assertEquals(2, Solution.add(-1, 3));
    }
}
```
<|Test End|>

## Question:
