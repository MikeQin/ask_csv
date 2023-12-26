from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI


load_dotenv('./.env') 
client = OpenAI()

def main():
  print('** Ask CSV **')
  st.set_page_config(page_title='Ask your CSV')
  st.header("Ask your CSV")

  user_csv = st.file_uploader('Upload your CSV file', type='csv')

  if user_csv is not None:
    user_question = st.text_input('Ask a question about your CSV: ')

    llm = OpenAI(temperature=0)
    agent = create_csv_agent(llm=llm, path=user_csv, verbose=True)

    if user_question is not None and user_question != "":
      response = agent.run(user_question)
      # st.write(f'Your question was: {user_question}')
      st.write(f'Answer: {response}')
      # What is the mean radius/area/smoothness of the malignant tumors?



if __name__ == "__main__":
  main()
