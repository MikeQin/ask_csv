from dotenv import load_dotenv #, dotenv_values
from openai import OpenAI

load_dotenv('./.env')  # take environment variables from .env.
# config = dotenv_values("./.env")
# print(config['OPENAI_API_KEY'])

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)