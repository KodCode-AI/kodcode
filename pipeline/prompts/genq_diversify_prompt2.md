## Task
Generate **persona-driven coding questions** that create engaging scenarios with realistic characters and situations.

## Objective
Take an existing coding question and create variations that:
- Feature a **specific persona** (a developer, engineer, or professional) with clear motivations
- Present **realistic scenarios** that this persona would encounter in their work or daily life
- Maintain the same core programming concepts and skills being tested
- **Use the specified programming language** consistently across all variations

## Guidelines

### Persona & Scenario Creation
- **Character Profile**: Create a specific person with name, role, background, and clear motivations
- **Real-world Context**: Situate problems in actual business scenarios, client requests, or technical challenges
- **Clear Stakes**: Establish what success or failure means for the persona
- **Industry Relevance**: Connect to specific domains (fintech, healthcare, e-commerce, gaming, etc.)

### Core Requirements
- Preserve the fundamental programming skills and concepts being assessed
- Ensure each variation is solvable with the same level of programming knowledge
- Maintain clear and self-contained problem descriptions
- **Use the target programming language** specified in the input

### Enhancement Focus
- **Engagement**: Create scenarios with personal/professional stakes and realistic deadlines
- **Complexity**: Add sophisticated constraints, multi-step processes, or optimization challenges
- **Language Features**: Utilize advanced features and best practices of the specified language

## Input Format
**Original Question**: {ORIGINAL_QUESTION}
**Programming Language**: {LANGUAGE}

## Output Requirements
Generate **one persona-driven variation** of the original question. The variation should:
1. Feature a **specific persona** with clear motivations and background
2. Present a **realistic scenario** this persona would encounter
3. Maintain the same core programming skills being tested
4. **Increase engagement** through relatable context and clear stakes
5. **Use the specified programming language** consistently
6. Feel like a natural, real-world situation from a different professional context
7. Be meaningfully different from the original and other variations
8. **Be completely self-contained** - the question itself should include all necessary context
9. Do not include sample solutions or implementation details in the question since this is meant to be a coding challenge for assessment

## Output Format
Please use the following output format for consistency.

<|Analysis Begin|>

[Write your analysis here]

<|Analysis End|>

<|Persona Begin|>

[Describe the specific persona - their name, role, background, and current situation]

<|Persona End|>

<|Scenario Begin|>

[Describe the realistic scenario and context that leads to the coding challenge]

<|Scenario End|>

<|Question Begin|>

[Write the coding question here. The question should be self-contained and include all the context from the persona and scenario so that users can understand the full situation without needing to see the separate persona and scenario sections.]

<|Question End|> 