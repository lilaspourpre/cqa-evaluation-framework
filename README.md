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


## Example Summary Evaluation
Example shows the summary produced by **Mixtral** model to compare **dell** and **ibm** for their **power of processors**. The summary was generated using the **third** prompt scenario. 

```
Summary:
Dell and IBM are technology giants, offering a diverse range of products and services. Dell, a prominent hardware manufacturer, provides a wide array of customizable PCs, laptops, and servers, often praised for their affordability and ease of use. IBM, on the other hand, has a strong focus on enterprise solutions, offering a comprehensive suite of software, services, and consulting. IBM is known for its robust mainframe computers and cognitive computing solutions, leveraging AI and analytics. Both companies have a global presence and cater to a variety of customers, from individuals to large enterprises. This comparison will focus on their key differences to determine which offers the better overall package. 

Comparison:

- Product Range:
   - Dell: Offers a broad range of customizable PCs, laptops, and servers for consumers and businesses. Known for affordability, ease of use, and flexibility in specifications.
   - IBM: Focuses on enterprise solutions, including mainframe computers, software, and cognitive computing. Provides robust hardware and advanced AI, analytics, and cloud services.

- Target Market:
   - Dell: Caters to a wide range of consumers, small businesses, and enterprises. Offers products suitable for various budgets and needs.
   - IBM: Primarily targets large enterprises and organizations with its comprehensive suite of advanced solutions.

- Strengths:
   - Dell:
     - Affordability: Known for providing quality products at competitive prices.
     - Customizability: Allows users to customize hardware specifications to meet specific needs.
     - Ease of Use: Dell products are often user-friendly and intuitive.

   - IBM:
     - Enterprise Solutions: Offers a one-stop shop for enterprises with advanced hardware, software, and consulting services.
     - Innovation: Invests heavily in R&D, leading to innovative solutions like Watson cognitive computing.
     - Mainframe Expertise: Renowned for robust and reliable mainframe computers.

Best Option: 
Tie
```
Example Summary.
- Generator model: **Mixtral** 
- Prompt scenario: **3** 
- object: **dell** and **ibm**
- aspect: **power of processors**. 


## Evaluation

Table below shows the evaluation of the example summary across all 15 criteria, done by a human expert and LLaMA-3 70b. For criterion C1, the introduction of the summary is pretty long and marked *0* by the human expert, but *1* by the LLaMA-3 70b, this is also a tricky decision in the absence of description in terms of word or sentence count.
For the sorting of arguments (C8), LLaMA-3 70b assigned *0*, while human annotation sees the aspects as sorted by general applicability. The last difference is the C9 criterion: the human annotation is stricter and assigns *0*, while LLaMA-3 70b assumes that all arguments are relevant.

| No. | Criteria description | Evaluation LLaMA-3 70b | Evaluation Human |
|-|-|-|-|
|  C1     | a short introduction is present: **0-1** | 1          |  <ins>0</ins>  |
|   C2     | there are defined aspects used for comparison in the whole comparison: **0-1**     | 1    | 1 |
|   C3     | the introduction mentions the most important comparison aspects: **0-1**  | 1      |   <ins>0</ins>  |
 |   C4     | the main body of comparison has good structure: **0-1**  | 1    | 1 |
  |  C5     | the main body of the comparison has defined aspect names: **0-1** | 1   | 1 |
  |  C6     | the main body of the comparison has defined aspect descriptions: **0-1**      | 1     | 1 |
  |  C7     | the final choice is given explicitly: **0-1**     |   <ins>0</ins>    |   <ins>0</ins> |
  |  C8     | the comparison aspects in the main body of the comparison are sorted by general applicability: **0-1**    |   <ins>0</ins>     | 1 |
   | C9     | each argument is relevant to the aspect of comparison (if any, otherwise is general and is not biased towards any aspect): **0-2**     | 2     |  <ins>0</ins> |
| C10    | each argument compares both objects: **0-2**      | 2     | 2 |
   | C11    |  here are no hallucinations or statements contradicting common knowledge: **0-2**       | 2    | 2 |
   | C12    | the comparison has proper language and is easy to follow: **0-2**     | 2    | 2 |
   | C13    | here are no repetitive statements or statements too similar to each other: **0-1**      | 1    | 1 |
   | C14    | the final answer is concluded from the statements in the main body and takes the main aspect (if there is one) into consideration: **0-1**        | <ins>0</ins>     |   <ins>0</ins>  |
   | C15    | the summary itself is not too short and not too long: **0-1**      | 1     | 1 |
     
Evaluation of summary from above.  <ins>**Underline**</ins> highlights the disagreement for the corresponding criteria.


Summary scoring criteria, with evaluation scores assigned by a human expert and GPT-4 (may be add both zero-shot and few-shot?) for the example summary. There are 15 rules with a total score of 19 points.

Scoring Criteria  |  Expert Score    |   GPT-4 Score |
|-|-|-|
|    1. a short introduction is present: 0-1 |   0     |  0 |
| - the introduction is missing or is too long - 0 points ||
|- the introduction is short and concise - 1 point ||
| 2. there are defined aspects used for comparison in the whole comparison: 0-1 |  0    | 0 |
 |  - the comparison is arbitrary with no specific aspects - 0 points ||
|  - the comparison uses specific aspects to compare objects - 1 point || 
|   3. the introduction mentions the most important comparison aspects: 0-1  |   0     |  0 |
| - no aspects are mentioned or no introduction - 0 points ||
| - several most important aspects are mentioned in the introduction - 1 point ||   
 |  4. the main body of comparison has good structure: 0-1  |   0     |  0 |
 |  - some aspects mix with others, the structure is harder to follow - 0 point ||
|  - the aspects are logically divided into separate aspects - 1 point ||   
| 5. the main body of the comparison has defined aspect names: 0-1  |   0     |  0 |
| - no aspect names are given, comparison is inconcrete - 0 points ||
 |   - main body has distinct aspect names - 1 point || 
| 6. the main body of the comparison has defined aspect descriptions: 0-1  |   0     |  0 |
  |  - no aspect descriptions are given, comparison is inconcrete - 0 points ||
   | - main body has distinct aspect descriptions - 1 point || 
  |  7. the final choice is given explicitly: 0-1 | 0 | 0|
   | - no explicit choice made or lengthy justification present - 0 points ||
   | - short and explicit choice made - 1 point ||
   |  8. the comparison aspects in the main body of the comparison are sorted by general applicability: 0-1 | 0 | 0 |
 |   - statements are not sorted at all - 0 points ||
  |  - statements are sorted by general/important statements first, specific statements closer to the end - 1 point ||
   | 9. each argument is relevant to the aspect of comparison \\(if any, otherwise is general and is not biased towards any aspect): 0-2 | 0 | 0|
   | - most arguments are irrelevant - 0 points||
   | - most arguments are relevant - 1 point ||
   | - all arguments are relevant - 2 points ||
|    10. each argument compares both objects: 0-2  | 0 | 0|
| - some arguments do not compare the objects - 0 points ||
 |   - some arguments give information only about one object - 1 points ||
  |  - all arguments compare both objects - 2 points ||
 |   11. there are no hallucinations or statements contradicting common knowledge: 0-2 | 0 | 0|
  |  - many hallucinations, serious factual inaccuracy - 0 points ||
  |  - some hallucinations, but mostly correct - 1 point ||
  |  - no hallucinations, factually correct - 2 points ||
|    12. the comparison has proper language and is easy to follow: 0-2 | 0 | 0|
 |   - hard to read, profanity present or illogical - 0 points ||
  |  - some grammar issues, broken logic - 1 point ||
   | - no grammar issues, good structure and logic - 2 points	 ||
| 13. there are no repetitive statements or statements too similar to each other: 0-1 | 0 | 0|
  | - some statements repeat others’ meaning very closely - 0 points ||
  |  - all statements are unique and do not repeat - 1 points	||
|  14. the final answer is concluded from the statements in the main body and takes the main aspect (if there is one) into consideration (if all statements favor object 1, then the answer is object 1,  if both objects are equally good or equally bad, then none of the objects is preferred and the answer is inconclusive): 0-1 | 0 | 0|
 | - the final answer is not concluded from the arguments or main aspect (if there is one) or no answer is given - 0 points ||
  | - the final answer is concluded from the majority of arguments and main aspect (if there is one) - 1 point ||  
  |  15. the summary itself is not too short and not too long: 0-1 | 0 | 0|
 |   - the summary is too short (less than 12 sentences) or too long (more than 20 sentences) - 0 points ||
|    - the summary is reasonably long (from 12 to 20 sentences) - 1 point	||






## Datasets Details

In addition to the answers created with 6 models and four prompt scenarios, we also assess previously available datasets. 

  - **Touché Dataset** (bondarenko:2022e) is a dataset created for the Touché Shared task on comparative questions. Given a comparison search topic with two comparison objects and a collection of text passages, the task was to retrieve relevant argumentative passages for one or both objects, and to detect the passages' stances with respect to the objects. The authors provided 50 search topics that described scenarios of personal decision making. Each of these topics had a title in terms of a comparative question, comparison objects for the stance detection of the retrieved passages, a description specifying the particular search scenario, and a narrative that served as a guideline for the assessors.
    
 - **Yahoo!Answer Dataset** (chekalina-etal-2021-better) comprises 28 answers. The authors use information extracted from Yahoo! Answers: they collect a subset of L6–Yahoo! Answers Comprehensive Questions and Answers version 1.0 retrieved from Yahoo! Webscope. %As opposed to the above-mentioned dataset, the mean token length of the answers is TODO.

 - **CAM 2.0 dataset** (shallouf-etal-2024-cam) is an automatically created dataset of comparative answers using the *``lmsys/vicuna-7b-v1.5''* model using a two-shot setup. The authors ask the model to write a comparison summary of objects and also provide a list of arguments extracted from CAM 2.0. The task is to summarize only relevant arguments and to put citations of the arguments inside the generated text to prevent hallucination. The number of summaries is 50.
% , as the questions for the task were taken from Yahoo!Answers.


Table below provides the examples of the samples from the datasets. 

| Dataset name  |  Example |
|-|-|
| Touché dataset | \{"question": "Which is better, a laptop or a desktop?", "pair": ["laptop", "desktop"]\}
| Yahoo!Answer Dataset  | How can you even ask this question yet? Only the Xbox 360 is out at the moment and that hasn't even been tested by gamers enough to see truely how good or rubbish it is. You need to ask the question again when all three systems are out! |
| CAM 2.0 dataset  | Microsoft and Sony are two major companies in the technology industry, with a significant presence in the gaming market. Some argue that Microsoft is better and faster than Sony, with updates going smoother and less frequent [2]. Microsoft is also considered to have a better SDK for games [3], and their conference was thought to have better pacing [4]. Additionally, some believe that Microsoft has a superior position over Sony in terms of software tools [9]. However, others argue that Sony is a superior hardware manufacturer, much better than both Nintendo and Microsoft [11]. The PS4 is physically superior to the Xbox One, with better design [12]. Sony is also believed to be working harder for gamers than Microsoft and Nintendo [10]. In terms of gaming, some argue that Microsoft is inferior to Sony [13], and that Sony is superior to Microsoft in every way possible [17]. Sony was also considered to be a bit smarter than Microsoft in terms of their approach to gaming [18]. Ultimately, the preference between Microsoft and Sony comes down to personal opinions and experiences. Some may prefer Microsoft for its software tools and updates, while others may prefer Sony for its hardware design and gaming experience. Arguments used: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20|

Samples from the external datasets assessed in the Comparative QA framework.

## Examples 

Example of a human summary, objects: **Google** and **Yahoo**.

```
**Summary:** 
When comparing Google Search and Yahoo, Google's dominance in the search engine market is undeniable due to its superior user experience, relevance of search results, integration with other services, and overall brand reputation.  
**Main Aspects of Comparison:** 
- User Interface: Google features a clean and minimalist design, while Yahoo search interface is more cluttered and more overwhelming [1,4]. 
- Search Quality: Google's search algorithm is renowned for its accuracy and relevance in delivering search results, outperforming Yahoo. 
- Search speed: Google search is known for its fast search results than Yahoo - Market Dominance: Google dominates the search engine market, giving users access to a vast database of information, in comparision to the Yahoo search, struggling to compete with Google. 
- User experience: Both Google and Yahoo Search are praised for their browsing experience [1]. 
- Features & Services: Google offers a wider range of integrated services and functionalities than Yahoo. [4] Both Google and Yahoo search may offer unique features or tools that enhance the search experience.
 - Mobile compatibility & Cross-platform integration: Google Search is more optimized for mobile devices, offering a better integration across various platforms than Yahoo Search.  
**Best Option:** Google
```

Example of another human summary, objects: **Google** and **Yahoo**. 
```
Summary: 
Google Search and Yahoo Search offer distinct user experiences, each with its strengths and weaknesses. While Google dominates the market, Yahoo Search presents competitive features and a pleasant interface, particularly highlighted in its integration with services like Flickr.  
Main Aspects of Comparison: 
- User experience: Yahoo search is considered to provide a nicer experience compared to Google search [1] 
- Past performance: Yahoo search was deemed better than Google search in the first half of 2008 [2] 
- Search quality: Yahoo search delivers more relevant results than Google search, highlighting its superiority [3], although one may argue that Google's search algorithms are often considered more sophisticated and effective [generated]. 
- Unique services: Yahoo's Flickr photo service surpasses Google's offerings, suggesting a wider range of services [4] 
- Visual appeal: Yahoo search may have a more visually appealing interface compared to Google search [generated] 
- Additional features: Yahoo search may offer unique features or tools that enhance the search experience [generated] 
- Search speed: Google search is known for its fast search results, which may be a crucial factor for some users [generated] 
- Customization Options: Yahoo Search provides extensive customization options, allowing users to tailor their search preferences. [generated] 
- Accessibility: Google Search is more widely accessible across various devices and platforms [generated].    
Best option: Yahoo
```


