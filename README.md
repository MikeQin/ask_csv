# OpenAI Learn

## Create Python Virtual ENV
Create venv
`python -m venv openai-env`

Activate
`openai-env/Scripts/activate`

## Install the OpenAI Python library

`pip install --upgrade openai`

## Setup API key for all projects

`setx OPENAI_API_KEY "api_key"`

## Install dotenv
Create .env with OPENAI_API_KEY=secret_key

Install:
`pip install python-dotenv`

## Install Dependent Libs
website: https://www.lfd.uci.edu/~gohlke/pythonlibs/
- frozenlist-1.3.0-py3-none-any.whl
- multidict-6.0.2-py3-none-any.whl

```
pip install streamlit
pip install frozenlist-1.3.0-py3-none-any.whl
pip install multidict-6.0.2-py3-none-any.whl
pip install langchain
pip install langchain_experimental
```
