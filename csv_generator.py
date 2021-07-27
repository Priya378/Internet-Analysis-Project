import csv
import parsing_file
import pandas as pd
df = pd.DataFrame(parsing_file.dic)
df.transpose().to_csv('data.csv', index=True)
