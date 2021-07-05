import csv
import parser
import pandas as pd
df = pd.DataFrame(parser.dic)
df.transpose().to_csv('data.csv', index=True)