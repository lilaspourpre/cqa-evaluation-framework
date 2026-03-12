# cqa-evaluation-framework

## Full Evaluation Prompt
```
  You are a helpful assistant.
    Task:
    - analyze the comparison given
    - for each criterion, assign points in the range given
    Criteria:
    1. a short introduction is present: 0-1
       - the introduction is missing or is too long - 0 points
       - the introduction is short and concise - 1 point
    2. there are defined aspects used for comparison: 0-1
       - the comparison is arbitrary with no specific aspects - 0 points
       - the summary uses specific aspects to compare objects - 1 point
    3. the introduction mentions the most important comparison aspects: 0-1
       - no aspects are mentioned or no introduction - 0 points
       - several most important aspects are mentioned in the introduction - 1 point
    4. the main body of the comparison has good structure: 0-1
       - some aspects mix with others, the structure is harder to follow - 0 point
       - the aspects are logically divided into separate aspects - 1 point
    5. the main body of the comparison has defined aspect names: 0-1
       - no aspect names are given, comparison is inconcrete - 0 points
       - main body has distinct aspect names - 1 point
    6. the main body of the comparison has defined aspect descriptions: 0-1
       - no aspect descriptions are given, comparison is inconcrete - 0 points
       - main body has distinct aspect descriptions - 1 point
    7. the final choice is given explicitly: 0-1
       - no explicit choice made or lengthy justification present - 0 points
       - short and explicit choice made - 1 point
    8. the comparison aspects in the main body of the comparison are sorted by general applicability: 0-1
       - statements are not sorted at all - 0 points
       - statements are sorted by general/important statements first, specific statements closer to the end - 1 point
    9. each argument is relevant to the subject of comparison: 0-2
       - most arguments are irrelevant - 0 points
       - most arguments are relevant - 1 point
       - all arguments are relevant - 2 points
    10. each argument compares both objects: 0-2
       - some arguments do not compare the objects - 0 points
       - some arguments give information only about one object - 1 point
       - all arguments compare both objects - 2 points
    11. there are no hallucinations or statements contradicting common knowledge: 0-2
       - many hallucinations, serious factual inaccuracy - 0 points
       - some hallucinations, but mostly correct - 1 point
       - no hallucinations, factually correct - 2 points
    12. the comparison has proper language and is easy to follow: 0-2
       - hard to read, profanity present or illogical - 0 points
       - some grammar issues, broken logic - 1 point
       - no grammar issues, good structure and logic - 2 points
    13. there are no repetitive statements or statements too similar to each other: 0-1
       - some statements repeat others' meaning very closely - 0 points
       - all statements are unique and do not repeat - 1 point
    14. the final answer is concluded from the statements in the main body and takes the main aspect (if there is one) into consideration (if all statements favor object 1, then the answer is object 1, if both objects are equally good or equally bad, then none of the objects is preferred and the answer is inconclusive): 0-1
       - the final answer is not concluded from the arguments or main aspect (if there is one) or no answer is given - 0 points
       - the final answer is concluded from the majority of arguments and main aspect (if there is one) - 1 point
    15. the summary itself is not too short and not too long: 0-1
       - the summary is too short (less than 12 sentences) or too long (more than 20 sentences) - 0 points
       - the summary is reasonably long (from 12 to 20 sentences) - 1 point
Output a python dictionary with the structure: {"n": score, "n+1": score}
    Write only the dictionary, do not write anything else
    Example 1:
    Summary:
    The Nintendo DS and PlayStation 3 are two iconic gaming consoles that revolutionized the gaming industry. While the DS focused on handheld gaming, the PS3 offered a high-definition gaming experience on a home console. Both devices have their unique features and strengths, making it challenging to determine the better option.
    Main Aspects of Comparison:
    - Graphics: The PS3 boasts superior graphics capabilities with its high-definition output, providing a more immersive gaming experience compared to the DS's smaller screen.
    - Game Library: The PS3 has a vast library of games, including popular titles like Uncharted" and "The Last of Us", while the DS offers a wide range of unique and innovative games such as "Mario Kart DS" and "The Legend of Zelda: Phantom Hourglass."
    - Online Capabilities: The PS3's online platform, PlayStation Network, offers robust multiplayer options and digital downloads, whereas the DS's online features are more limited.
    - Portability: The DS's handheld design allows for gaming on the go, making it a convenient option for travel or commutes, while the PS3 is limited to home use.
    - Controller Design: The DS features a touchscreen and stylus for innovative gameplay, while the PS3's DualShock controller provides a more traditional gaming experience.
    Best Option:
    PS3
    Scoring 1:
    {1: 1,	2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 2, 12: 2, 13: 1, 14: 1, 15: 1}
    Question: What is better{aspect_text}: {object1} or {object2}?
    Comparative answer:
    {comparison}
```
Full Evaluation Prompt used for directing an LLM to analyze comparative summaries in line with our 15 criteria. This example also includes a sample summary evaluation for few-shot prompting.

