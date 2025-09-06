## Task:
Please Answer the question and generate unit tests to verify your answer.

## Output Format:
Your solution and unit tests should be presented in markdown C# code format within the specified sections below. Ensure your code is within code blocks. Use assertion for the tests.

<|Solution Begin|>
[Solution Code in C#]
<|Solution End|>
<|Test Begin|>
[Unit Test Code in C#]
<|Test End|>

## Example
Below is an example output format implementing a simple a + b function.

<|Solution Begin|>
```csharp
using System;
using System.Diagnostics;

public class Solution
{
    // Returns the sum of a and b.
    public static int Add(int a, int b)
    {
        return a + b;
    }
}
```
<|Solution End|>

<|Test Begin|>
```csharp
using System;
using System.Diagnostics;

public class Tests
{
    public static void Main()
    {
        var candidate = Solution.Add;
        
        // Test positive numbers
        Debug.Assert(candidate(2, 3) == 5);
        Debug.Assert(candidate(10, 15) == 25);
        
        // Test with zero
        Debug.Assert(candidate(0, 5) == 5);
        Debug.Assert(candidate(5, 0) == 5);
        Debug.Assert(candidate(0, 0) == 0);
        
        // Test negative numbers
        Debug.Assert(candidate(-1, -1) == -2);
        Debug.Assert(candidate(-5, -10) == -15);
        
        // Test mixed sign numbers
        Debug.Assert(candidate(-1, 3) == 2);
        Debug.Assert(candidate(10, -5) == 5);
        Debug.Assert(candidate(-10, 5) == -5);
        
        Console.WriteLine("All tests passed!");
    }
}
```
<|Test End|>

## Question:
