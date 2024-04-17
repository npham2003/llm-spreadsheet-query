# LLM Spreadsheet Query POC

This repository is a proof of concept for interfacing with an excel spreadsheet through langchain and an LLM. 

## How to run

- First execute the command:

  - `pip install -r requirements.txt`

  - This installs all necessary python packages.

- Inside main.py, set the OpenAI key to your key.

- Then execute the program using:
  - `python main.py`

- The program will run until you type quit and hit Enter.

## How to Change the Excel Spreadsheet

- Add the xlsx file to the content folder
- Change the file_name string on line 9 of main.py to the name of your file.
  - Do not include the file extension

