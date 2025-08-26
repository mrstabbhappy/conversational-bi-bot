from llm import ask_gpt
import pandas as pd

def get_query_from_question(question, df_sample):
    cols = ", ".join(df_sample.columns)
    sample = df_sample.head(3).to_dict()

    prompt = f"""
You are a Python data analyst.

The user is asking a question about a pandas DataFrame named `df`.
The DataFrame has the following columns: {cols}
Here is a sample of the data:
{sample}

Respond ONLY with valid Python code.
Use the existing variable `df` (do NOT recreate it).
Assign the final answer to a variable called `result`.

Example:
result = df['Amount'].sum()

Now generate code to answer:
"{question}"
    """

    return ask_gpt(prompt)
