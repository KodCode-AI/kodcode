## Task
Conduct a {LANGUAGE} **Coding Question Quality Assessment** across six key dimensions to ensure it meets high standards for programming education and evaluation.

## Objective
Analyze the provided coding question and assess its quality across six critical metrics to determine its effectiveness as a programming assessment tool.

## Assessment Criteria

### 1. Question Quality
**What to Evaluate**: Clarity, comprehensibility, and overall construction of the question statement.

**Rating Guidelines**:
- **very poor**: Unclear, ambiguous, or poorly constructed question
- **poor**: Some clarity issues, missing important context
- **average**: Clear and understandable, but could be more specific or engaging
- **good**: Well-constructed, clear, specific, and realistic
- **excellent**: Exceptionally clear, detailed, engaging, and professionally written

### 2. Question Difficulty
**What to Evaluate**: The complexity level and cognitive demand of the programming problem.

**Rating Guidelines**:
- **very easy**: Basic syntax and simple logic, suitable for beginners
- **easy**: Fundamental programming concepts with straightforward implementation
- **medium**: Requires problem-solving skills and intermediate programming knowledge
- **hard**: Complex algorithms, advanced data structures, or sophisticated logic required
- **very hard**: Expert-level programming challenges requiring deep algorithmic thinking

### 3. Test Correctness
**What to Evaluate**: Accuracy and validity of the provided test cases.

**Rating Guidelines**:
- **very poor**: Tests are incorrect, fail to compile, or test wrong functionality
- **poor**: Tests have significant errors or don't properly validate the solution
- **average**: Tests are mostly correct but may have minor issues
- **good**: Tests are accurate and properly validate the expected behavior
- **excellent**: Tests are comprehensive, accurate, and demonstrate best practices

### 4. Test Coverage
**What to Evaluate**: Completeness of test cases in covering different scenarios and edge cases.

**Rating Guidelines**:
- **very poor**: Minimal or no test coverage, missing critical test cases
- **poor**: Basic test coverage with significant gaps
- **average**: Adequate coverage of main scenarios but missing edge cases
- **good**: Comprehensive coverage including edge cases and boundary conditions
- **excellent**: Thorough coverage of all scenarios, edge cases, and error conditions

### 5. Solution Correctness
**What to Evaluate**: Accuracy and correctness of the provided solution.

**Rating Guidelines**:
- **very poor**: Solution is completely incorrect or doesn't solve the problem
- **poor**: Solution has major errors or significant logical flaws
- **average**: Solution is mostly correct but may have minor issues
- **good**: Solution is correct and properly implements the required functionality
- **excellent**: Solution is optimal, efficient, and demonstrates best practices

### 6. Solution Conciseness
**What to Evaluate**: Efficiency and elegance of the solution implementation.

**Rating Guidelines**:
- **very poor**: Solution is unnecessarily verbose, inefficient, or poorly structured
- **poor**: Solution could be significantly simplified or optimized
- **average**: Solution is reasonably concise but could be improved
- **good**: Solution is well-structured and appropriately concise
- **excellent**: Solution is elegant, efficient, and demonstrates optimal implementation

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


## Output Requirements

Provide analysis with detailed reasoning BEFORE scores for each of the six metrics.

## Output
Provide your response in the following XML format:

<response>
  <question_quality>
    <reasoning>
      <!-- Detailed explanation covering clarity, comprehensibility, and construction quality -->
    </reasoning>
    <rating><!-- Rating: very poor, poor, average, good, excellent --></rating>
  </question_quality>
  
  <question_difficulty>
    <reasoning>
      <!-- Detailed explanation of complexity level and cognitive demand -->
    </reasoning>
    <rating><!-- Rating: very easy, easy, medium, hard, very hard --></rating>
  </question_difficulty>
  
  <test_correctness>
    <reasoning>
      <!-- Detailed explanation of test accuracy and validity -->
    </reasoning>
    <rating><!-- Rating: very poor, poor, average, good, excellent --></rating>
  </test_correctness>
  
  <test_coverage>
    <reasoning>
      <!-- Detailed explanation of test completeness and edge case coverage -->
    </reasoning>
    <rating><!-- Rating: very poor, poor, average, good, excellent --></rating>
  </test_coverage>
  
  <solution_correctness>
    <reasoning>
      <!-- Detailed explanation of solution accuracy and functionality -->
    </reasoning>
    <rating><!-- Rating: very poor, poor, average, good, excellent --></rating>
  </solution_correctness>
  
  <solution_conciseness>
    <reasoning>
      <!-- Detailed explanation of solution efficiency and elegance -->
    </reasoning>
    <rating><!-- Rating: very poor, poor, average, good, excellent --></rating>
  </solution_conciseness>
</response> 