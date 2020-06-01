"""
This file prints each cell of dataframe individually
"""

import pandas as pd

input_csv_df = pd.read_csv('input.csv', header=None)

input_fields = input_csv_df.loc[0]

output_list = [] # each row is created in this list then appended to output dataframe

output_df = pd.DataFrame(columns=input_fields)

# productname,category1,category2,category3,image1,image2,description,price

number_of_rows = len(input_csv_df)

for row in range(number_of_rows):             # for each row in dataframe
  current_row = input_csv_df.loc[row]         # variable for current row of iteration
  for index, cell in enumerate(current_row):  # iterate though index and cells
    input_field_name = input_fields[index]    # current: productname,category1,category2,category3,image1,image2,description,price

    if cell == input_field_name: # if cell is a field name it needs to be skipped
      pass
    else:


      if index == 7:
        output_list.append(cell) # add cell to list

        output_df.loc[len(output_df)] = output_list # add list to data frame
        output_list = [] # reset list
      else: 

        output_list.append(cell) # add cell to list

output_df.to_csv('output.csv', index=False)