"""
This file prints each cell of dataframe individually
"""

import pandas as pd

input_csv_df = pd.read_csv('input.csv', header=None)

# productname,category1,category2,category3,image1,image2,description,price
input_fields = input_csv_df.loc[0]

number_of_rows = len(input_csv_df)

for row in range(number_of_rows):             # for each row in dataframe
  current_row = input_csv_df.loc[row]         # variable for current row of iteration
  for index, cell in enumerate(current_row):  # iterate though index and cells
    input_field_name = input_fields[index]    # current: productname,category1,category2,category3,image1,image2,description,price
    print(cell)