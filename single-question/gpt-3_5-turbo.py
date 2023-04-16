from pathlib import Path

import openai
import yaml

if __name__ == '__main__':
    """
    The example with `gpt-3.5-turbo` model.
    """
    base_directory = Path(__file__).parent.parent

    with open(f"{base_directory}/openai.yaml", "r") as openai_yaml:
        config = yaml.load(openai_yaml, Loader=yaml.FullLoader)

    openai.api_key = config['OPENAI']['API_KEY']

    model_engine = "gpt-3.5-turbo"
    prompt = "this is test. what is the token? how many did you recognize it?"

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are my home manager."},
            {"role": "user", "content": "Can you recommend me the menu for dinner?"},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
