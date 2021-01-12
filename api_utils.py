import pandas as pd
import numpy as np

# check headers


# Check that CSV is in a required format
df = pd.read_csv("data1.csv", sep=r'\s*,\s*', engine='python')

# handle duplicated rows
df = df.drop_duplicates()

# replace empty strings with null values


# check mandatory fields
df.dropna(subset=["race_type", "race_venue", "race_start_time"], inplace=True)

'''Attributes that are optional:
    - Race number
    - Race name
    - Must have either one of them
'''

row_index, col_index = np.where(pd.isnull(df))

# assert col_index is in range 1-2

def get_duplicated_index(row_index):
    curr = -1
    index = []
    for item in row_index:
        if item == curr:
            # print("duplicate")
            index.append(item)
        curr = item
    
    return index

duplicated_index = get_duplicated_index(row_index)
df.drop(df.index[duplicated_index], inplace=True)

# sorting by start time