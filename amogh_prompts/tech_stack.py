import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def tech_stack_model(string):
    """ To evaluate how well the product spec lists their tech stack

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the input
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following paragraph is the technology stack section of a product specification. Evaluate how well the technology stack has been written and give specific feedback on what can be improved. Write several in-depth sentences.\n{string}",
            temperature = 1,
            max_tokens = 512,
            top_p = 0.5,
            frequency_penalty = 0,
            presence_penalty = 1
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"tech_stack: {e}" # placeholder for now


# for internal testing

"""TEST_INPUT = "- Python (Discord.py, Django)\
- OpenAI’s GPT-3 API\
- Amazon EC2"

print(tech_stack_model(TEST_INPUT))"""
