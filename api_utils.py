import pandas as pd
import numpy as np
import datetime as dt

def clean_data(filename):
    # TODO: check headers

    # Check that CSV is in a required format
    # and enforce the necessary types
    df = pd.read_csv(filename, sep=r'\s*,\s*', engine='python', na_values=[""],
        dtype={"race_type": "category", "race_number": "Int64", 
        "race_name": "string", "race_venue": "string"}, 
        parse_dates=[4], date_parser=pd.to_datetime)

    # handle duplicated rows
    df = df.drop_duplicates()

    # check mandatory fields
    df.dropna(subset=["race_type", "race_venue", "race_start_time"], inplace=True)

    '''Attributes that are optional:
        - Race number
        - Race name
        - Must have either one of them
    '''

    row_index, col_index = np.where(pd.isnull(df))

    # assert col_index is in range 1-2
    def _get_duplicated_index(row_index):
        curr = -1
        index = []
        for item in row_index:
            if item == curr:
                # print("duplicate")
                index.append(item)
            curr = item
        
        return index

    duplicated_index = _get_duplicated_index(row_index)
    df.drop(df.index[duplicated_index], inplace=True)

    # Assume: only require the today's race with the time
    # Select Next-to-jump races for today only
    # TODO: do not select past races
    date_today = dt.date.today()

    selected_data = df[df.race_start_time.dt.date == date_today]

    # sort the races
    selected_data = selected_data.sort_values(by="race_start_time")

    # require only the time
    selected_data["race_start_time"] = selected_data.race_start_time.dt.strftime("%H.%M")

    # TODO: pretty print
    print(selected_data)

    return selected_data

print(clean_data("data1.csv"))