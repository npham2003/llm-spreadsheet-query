import pandas as pd
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
import os
import openpyxl

os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY-HERE"

file_name="excel_file_example"

xls_file = r'content/'+file_name+r'.xlsx'
output_csv = r'content/'+file_name+r'.csv'

# Read the XLS file using pandas and openpyxl as the engine
data = pd.read_excel(xls_file, engine='openpyxl')

# Save the data as a CSV file
data.to_csv(output_csv, index=False)

# create a csv agent with langchain and openai. make sure temperature is 0 to prevent hallucinations 
agent = create_csv_agent(OpenAI(temperature=0), r'content/'+file_name+r'.csv', verbose=True)
question = ""

while question.casefold()!="Quit".casefold():
    question = input("Type a question or type quit to exit: ")
    if question.casefold()!="Quit".casefold():
        agent.invoke(question)