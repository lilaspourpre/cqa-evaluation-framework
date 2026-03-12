import pandas as pd
import click
import transformers
import torch
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import InferenceClient


def get_predictor(model_name: str, key: str):
    if 'gpt' in model_name:
        model = OpenAI(api_key=key)
        return lambda x, y : gpt_predict_answer(x, model, y)
    elif '70' in model_name:
        model = InferenceClient(api_key=key)
        return lambda x,y : hf_predict_answer(x, model, y)
    else:
        model = transformers.pipeline(
            "text-generation",
            model=model_name,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return lambda x, y: llm_predict_answer(x, model, tokenizer, y)

def gpt_predict_answer(messages, model, num_regens):
    completion = client.chat.completions.create(model=model, messages=messages, n=num_regens)
    return completion.choices[0].message.content

def llm_predict_answer(messages, model, tokenizer, num_regens):
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    outputs = model(
        messages,
        max_new_tokens=256,
    )
    return outputs[0]["generated_text"][-1]

def hf_predict_answer(messages, model, num_regens):
    completion = model.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct", 
    	messages=messages,
        max_tokens=256
    )
    return completion.choices[0].message.content


@click.command()
@click.option("--key", default="0")
@click.option("--input-filepath", required=True)
@click.option("--output-filepath", required=True)
@click.option("--model", default="gpt-4")
@click.option("--num-regens", default=1)
@click.option("--fewshot", default=True)
def main(key: str, input_filepath: str, output_filepath: str, model: str, num_regens: int, fewshot: bool):
    predictor = get_predictor(model, key)
    df = pd.read_json(input_filepath)

    completions_dict = {}
    for index in tqdm(range(len(df)), desc='Processing rows'): #)
        object1 = df.loc[index, 'object1']
        object2 = df.loc[index, 'object2']
        aspect = df.loc[index, 'aspect']
        aspect_text = f" when comparing regarding {aspect}" if aspect != '' else ''
        comparison = df.loc[index, "comparison"]
        content = [
            'You are a helpful assistant.\n',
            'Task:\n',
            '- analyze the comparison given\n',
            '- for each criterion, assign points in the range given\n',
            'Criteria:\n',
            '1. a short introduction is present: 0-1\n',
            '   * the introduction is missing or is too long - 0 points\n',
            '   * the introduction is short and concise - 1 point\n',
            '2. there are defined aspects used for comparison: 0-1\n',
            '   * the comparison is arbitrary with no specific aspects - 0 points\n',
            '   * the summary uses specific aspects to compare objects - 1 point\n',
            '3. the introduction mentions the most important comparison aspects: 0-1\n',
            '   * no aspects are mentioned or no introduction - 0 points\n',
            '   * several most important aspects are mentioned in the introduction - 1 point\n',
            '4. the main body of the comparison has good structure: 0-1\n',
            '   * some aspects mix with others, the structure is harder to follow - 0 point\n',
            '   * the aspects are logically divided into separate aspects - 1 point\n',
            '5. the main body of the comparison has defined aspect names: 0-1\n',
            '   * no aspect names are given, comparison is inconcrete - 0 points\n',
            '   * main body has distinct aspect names - 1 point\n',
            '6. the main body of the comparison has defined aspect descriptions: 0-1\n',
            '   * no aspect descriptions are given, comparison is inconcrete - 0 points\n',
            '   * main body has distinct aspect descriptions - 1 point\n',
            '7. the final choice is given explicitly: 0-1\n',
            '   * no explicit choice made or lengthy justification present - 0 points\n',
            '   * short and explicit choice made - 1 point\n',
            '8. the comparison aspects in the main body of the comparison are sorted by general applicability: 0-1\n',
            '   * statements are not sorted at all - 0 points\n',
            '   * statements are sorted by general/important statements first, specific statements closer to the end - 1 point\n', 
            '9. each argument is relevant to the subject of comparison: 0-2\n',
            '   * most arguments are irrelevant - 0 points\n', 
            '   * most arguments are relevant - 1 point\n', 
            '   * all arguments are relevant - 2 points\n', 
            '10. each argument compares both objects: 0-2\n',
            '   * some arguments do not compare the objects - 0 points\n', 
            '   * some arguments give information only about one object - 1 points\n', 
            '   * all arguments compare both objects - 2 points\n', 
            '11. there are no hallucinations or statements contradicting common knowledge: 0-2\n',
            '   * many hallucinations, serious factual inaccuracy - 0 points\n',
            '   * some hallucinations, but mostly correct - 1 point\n',
            '   * no hallucinations, factually correct - 2 points\n',
            '12. the comparison has proper language and is easy to follow: 0-2\n',
            '   * hard to read, profanity present or illogical - 0 points\n',
            '   * some grammar issues, broken logic - 1 point\n',
            '   * no grammar issues, good structure and logic - 2 points \n',
            '13. there are no repetitive statements or statements too similar to each other: 0-1\n',
            '   * some statements repeat others’ meaning very closely - 0 points\n',
            '   * all statements are unique and do not repeat - 1 points\n',
            '14. the final answer is concluded from the statements in the main body (if all statements favor object 1, then the answer is object 1, if both objects are equally good or equally bad, then none of the objects is preferred and the answer is inconclusive): 0-1\n',
            '   * the final answer is not concluded from the arguments or no answer is given - 0 points\n',
            '   * the final answer is concluded from the majority of arguments - 1 point\n',
            '15. the summary itself is not too short and not too long: 0-1\n',
            '   * the summary is too short (less than 12 sentences) or too long (more than 20 sentences) - 0 points\n',
            '   * the summary is reasonably long (from 12 to 20 sentences) - 1 point\n',
            'Output a python dictionary with the structure: {"n": score, "n+1": score}\n',
            'Write only the dictionary, do not write anything else\n',
            f'Question: What is better{aspect_text}: {object1} or {object2}?\n',
            'Comparative answer:\n',
            f'{comparison}\n'
            ]

        if fewshot:
           examples = [
                'Example 1:',
                "Summary:",
                "The Nintendo DS and PlayStation 3 are two iconic gaming consoles that revolutionized the gaming industry. While the DS focused on handheld gaming, the PS3 offered a high-definition gaming experience on a home console. Both devices have their unique features and strengths, making it challenging to determine the better option.",
                "Main Aspects of Comparison:",
                "- Graphics: The PS3 boasts superior graphics capabilities with its high-definition output, providing a more immersive gaming experience compared to the DS's smaller screen.",
                '- Game Library: The PS3 has a vast library of games, including popular titles like "Uncharted" and "The Last of Us", while the DS offers a wide range of unique and innovative games such as "Mario Kart DS" and "The Legend of Zelda: Phantom Hourglass."',
                "- Online Capabilities: The PS3's online platform, PlayStation Network, offers robust multiplayer options and digital downloads, whereas the DS's online features are more limited.",
                "- Portability: The DS's handheld design allows for gaming on the go, making it a convenient option for travel or commutes, while the PS3 is limited to home use.",
                "- Controller Design: The DS features a touchscreen and stylus for innovative gameplay, while the PS3's DualShock controller provides a more traditional gaming experience.",
                "Best Option:",
                "PS3",
                'Scoring 1:',
                '{1: 1,	2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 2, 12: 2, 13: 1, 14: 1, 15: 1}',
                'Example 2:',
                "Based on the provided list of arguments, here's a comparison between hybrid and diesel:",
                "**Arguments in favor of diesel:**",
                "1. Diesel engines are superior to hybrid systems.",
                "2. Diesel still superior to hybrid.",
                "3. In terms of fuel consumption and other environmental performance, hybrid buses are not superior to ordinary diesel buses.",
                "4. Diesel is currently a little bit better than hybrid technology in terms of efficiency.",
                "5. Diesel is slower than the hybrid but more responsive.",
                "6. Diesel is better for the environment than hybrid technology.",
                "**Arguments in favor of hybrid:**",
                "1. Hybrid technology is superior to diesel fuel imo.",
                "2. Hybrid buses are superior to ordinary diesel buses in terms of fuel consumption and other environmental performance.",
                "3. Hybrid buses attain 25% greater fuel mileage and achieve better acceleration than diesel buses.",
                "4. Hybrid-electrics offer a smoother ride than diesel buses.",
                "5. The Hybrid is much quicker than the diesel.",
                "6. Hybrid cars are not grossly inferior to diesel powered cars.",
                "7. Hybrid technology is far, far better for the environment than diesel.",
                "**Neutral arguments:**",
                "1. Gas hybrid is a much easier transition than diesel.",
                "2. Let's pretend the hybrid factor is still optimal for vehicles (or better yet, let's pretend the far superior clean diesel engine doesn't exist) and talk about the little Toyota's image.",
                "3. Unlike inferior leathers that are dyed with chemicals, or diesel - vegetable dyes bring out the natural leather smell over time and are better for the Environment than hybrid chemical dyes.",
                "It's clear that both diesel and hybrid have their advantages and disadvantages. Diesel engines are often considered more efficient and responsive, while hybrid technology is often seen as better for the environment and offering a smoother ride. Ultimately, the choice between diesel and hybrid depends on individual preferences and priorities.",
                'Scoring 2:',
                '{1: 0,	2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 2, 10: 2, 11: 2, 12: 2, 13: 0, 14: 0, 15: 1}',
                'Example 3:',
                "**Summary**",
                "In this comparison, we will analyze the quality of photos taken with Nikon and Sigma lenses. While both brands have their strengths and weaknesses, our analysis reveals that Nikon lenses generally produce higher-quality images. With superior build quality, better optics, and faster focusing, Nikon lenses outperform their Sigma counterparts.",
                "**Main Aspects of Comparison**",
                "• **Build Quality**: Nikon's build quality is superior to Sigma's, with a more solid and durable construction [1].",
                "• **Optics**: Sigma's 24-105mm lens has better optics than Canon's 24-105mm kit lens and Nikon's 24-120mm lens [2].",
                "• **Wide-Angle Lenses**: Nikon's 14mm-24mm zoom is superior to Sigma's 14mm f2.8 lens and slightly better than Nikon's 14mm f2.8 lens [3].",
                "• **Zoom Lenses**: Nikon's 10-24mm lens is more useful, better built, and sharper than Sigma's 10-20mm lens [4].",
                "• **Macro Lenses**: Sigma's 17-70mm lens has a better range, faster focusing, and is cheaper than Nikon's equivalent lens [5].",
                "• **Focusing Speed**: Sigma's lenses are faster focusing than Nikon's 1.4G lens at low apertures [6].",
                "• **Telephoto Lenses**: Nikon's 80-400mm lens is slightly lighter and better appointed than Sigma's equivalent lens [7].",
                "**Best Option**",
                "Nikon",
                "**Used Arguments**",
                "1. [1]",
                "2. [2]",
                "3. [3]",
                "4. [4]",
                "5. [5]",
                "6. [6]",
                "7. [7]",
                'Scoring 3:',
                '{1: 1,	2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 1, 10: 2, 11: 2, 12: 2, 13: 1, 14: 0, 15: 0}',
           ]
           for l in examples:
               content.insert(-3, l)

        content = '\n'.join(content)

        messages=[
            {"role": "system", "content": "You are an expert summary reviewer."},
            {"role": "user", "content": content}
        ]
        response = predictor(messages, num_regens)
        print(response)
        completions_dict[index] = {
        "object1": object1, 
        "object2": object2, 
        "aspect": aspect, 
        "comparison": comparison, 
        "score_dict": response
        }   
    
    out_df = pd.DataFrame(completions_dict)
    out_df.to_json(output_filepath, orient='records')


if __name__ == "__main__":
  main()