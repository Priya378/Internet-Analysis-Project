"""
Python file to generate csv to be used as dataset
"""
import pandas as pd
import parsing_file
df = pd.DataFrame(parsing_file.dic)
df.transpose().to_csv('data.csv', index=True)
