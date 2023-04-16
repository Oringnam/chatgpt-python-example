# Setup
## Constraints
- the repository build with python 3.10
- any other dependencies, check [requirements.txt](requirements.txt)

## Install Python Packages
```bash
pip install -r requirements.txt
```

## Set Your API Key
First, Copy the [[openai.yaml.template](openai.yaml.template)] and save it as `openai.yaml`.

Then, replace the `API_KEY` field with your own API key value.
```bash
OPENAI:
  API_KEY: ***
```

# Example Run
```bash
python3 single-question/gpt-3_5-turbo.py
```

# Reference
## API Guide from openai
- https://platform.openai.com/docs/api-reference/completions/create