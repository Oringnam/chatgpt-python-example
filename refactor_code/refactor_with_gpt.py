import json
import re
from pathlib import Path

import openai
import yaml


def send_message_to_chatgpt(prev_messages, new_question):
    prev_messages.append({"role": "user", "content": new_question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prev_messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    assistant_message = response.choices[0].message

    answer = {'Question': new_question, 'Answer': assistant_message.content}
    print(json.dumps(answer, indent=4))
    return assistant_message.content


def parse_message(message):
    pattern = r"```(.*?)```"
    matches = re.findall(pattern, message, re.DOTALL)
    return matches[0]


if __name__ == '__main__':
    """
    The example for chaining questions.
    """
    base_directory = Path(__file__).parent.parent

    with open(f"{base_directory}/openai.yaml", "r") as openai_yaml:
        config = yaml.load(openai_yaml, Loader=yaml.FullLoader)

    openai.api_key = config['OPENAI']['API_KEY']

    messages = [
        {"role": "system", "content": """You are a helpful assistant for develop. 
        You can refactor python code. 
        The entire of refactored code inside the '```' single block."""}
    ]

    ugly_codes = []
    with open('ugly_code.py', 'r') as ugly_code_files:
        ugly_codes = [line for line in ugly_code_files]

    ugly_code = '\n'.join(ugly_codes)

    print("The ugly code")
    print("=====")
    print(ugly_code)
    print("=====")

    asked = f"Refactor the duplication with below requested code. ```\n {ugly_code}\n```"
    response = send_message_to_chatgpt(messages, asked)

    refactored_code = parse_message(response)
    print(refactored_code)

    with open('refactored_code.py', 'w') as refactored_code_files:
        refactored_code_files.write(refactored_code)
