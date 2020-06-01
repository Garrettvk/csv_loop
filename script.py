"""
This file prints each cell of dataframe individually
"""

import pandas as pd

input_csv_df = pd.read_csv('input.csv')

number_of_rows = len(input_csv_df)

for row in range(number_of_rows):     # for each row in dataframe
  current_row = input_csv_df.loc[row] # variable for current row of iteration
  for cell in current_row:            # print every cell in row
    print(cell)