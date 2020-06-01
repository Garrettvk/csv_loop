"""
This file prints each cell of dataframe individually
"""

import pandas as pd
import time

input_csv_df = pd.read_csv('input.csv') # df = the csv file we want to read

number_of_rows = len(input_csv_df)

for row in range(number_of_rows):
  current_row = input_csv_df.loc[row]
  for row in current_row:
    print(row)