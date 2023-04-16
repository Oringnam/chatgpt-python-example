from pathlib import Path

import openai
import yaml

if __name__ == '__main__':
    """
    The example with `text-davinci-003` model.
    """
    base_directory = Path(__file__).parent.parent

    with open(f"{base_directory}/openai.yaml", "r") as openai_yaml:
        config = yaml.load(openai_yaml, Loader=yaml.FullLoader)

    openai.api_key = config['OPENAI']['API_KEY']

    model_engine = "text-davinci-003"
    prompt = """
    We recently passed one million digital-only subscribers, reflecting the remarkable bond that The Times has built with readers on our digital platforms. They join our 1.1 million print-and-digital subscribers.
    
    ====
    
    What are tokens from the article? Tell me top 10 token what you analyze it. Then, tell me entire number of tokens in the article?
    """

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=2,
        stop=None,
        temperature=0.1,
    )

    print("=== First response ===")
    response01 = completion.choices[0].text
    print(response01)

    print("\n\n")

    print("=== Second response ===")
    response02 = completion.choices[1].text
    print(response02)
