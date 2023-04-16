import json
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
    prev_messages.append(assistant_message)
    return prev_messages


if __name__ == '__main__':
    """
    The example for chaining questions.
    """
    base_directory = Path(__file__).parent.parent

    with open(f"{base_directory}/openai.yaml", "r") as openai_yaml:
        config = yaml.load(openai_yaml, Loader=yaml.FullLoader)

    openai.api_key = config['OPENAI']['API_KEY']

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    question1 = "What is the capital of France?"
    chain_messages = send_message_to_chatgpt(messages, question1)

    question2 = "What is the population of Paris?"
    chain_messages = send_message_to_chatgpt(chain_messages, question2)

    question3 = "What I asked you before? Tell me my all this conversation's questions and your answer again."
    chain_messages = send_message_to_chatgpt(chain_messages, question3)
