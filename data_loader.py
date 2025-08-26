import pandas as pd

def load_data(path='BITest.xlsx'):
    df = pd.read_excel(path)
    return df