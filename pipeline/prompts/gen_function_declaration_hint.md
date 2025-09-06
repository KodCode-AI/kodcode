## Task
Generate a function declaration hint for a {LANGUAGE} coding problem with detailed analysis.

## Objective
Analyze the provided question, solution, and test code to determine the exact function declaration required, then provide a properly formatted declaration hint to help ensure generated code matches the unit tests.

## Question Analysis

### Question Content
```
{QUESTION}
```

### Solution
```
{SOLUTION}
```

### Test Cases
```
{TEST}
```

### Programming Language: {LANGUAGE}

## Instructions
Carefully analyze the solution and test code to extract the precise function declaration. Consider:
- Function name (exact spelling and case)
- Parameter names and types
- Return type
- Language-specific modifiers (public, static, etc.)
- Special syntax requirements for the target language

**Important**: If the problem requires designing classes, multiple functions, or focuses primarily on output/side effects, provide a flexible hint that helps match the unit tests instead of a strict function declaration.

## Language-Specific Declaration Formats

**Go**: `func FunctionName(paramType paramName) returnType`
**Java**: `public static returnType functionName(paramType paramName)`
**C++**: `returnType functionName(paramType paramName)`
**JavaScript**: `function functionName(paramName)`
**TypeScript**: `function functionName(paramName: paramType): returnType`
**C#**: `public static returnType FunctionName(paramType paramName)`
**Rust**: `pub fn function_name(param_name: ParamType) -> ReturnType`
**Python**: `def function_name(param_name: ParamType) -> ReturnType`

## Output Requirements

Provide detailed reasoning about the function declaration analysis, then give the exact declaration in the specified XML format.

## Output
Provide your response in the following XML format:

<response>
  <declaration_analysis>
    <reasoning>
      <!-- Detailed analysis covering:
           For single function problems:
           - Function name identification from solution/tests
           - Parameter analysis (types, names, count)
           - Return type determination
           - Language-specific requirements
           - Any special considerations or edge cases
           
           For complex problems (classes, multiple functions, etc.):
           - Analysis of what structures/methods are needed
           - Key interface requirements from tests
           - Important naming conventions or patterns
           - Critical implementation details to match tests
      -->
    </reasoning>
    <declaration><!-- For single functions: exact function declaration in language-specific format
                     For complex problems: flexible hint covering key structures, method names, return types, or patterns needed to pass unit tests --></declaration>
  </declaration_analysis>
</response>
