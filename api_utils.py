import pandas as pd
import numpy as np
import datetime as dt

# TODO: pretty print
def pretty_print_tabular():

 
    return

def clean_data(filename):
    '''
        Input   - filename
        Output  - race_type, race_info (race_number and race_name concatenated), race_venue, race_time

        race_info attribute:
            if race_number is not present, print:
                <race_name>
            if race_name is not present, print:
                Race <race_number>
            if both are present, print:
                Race <race_number> - <race_name>
    '''

    # Check that CSV is in a required format and enforce the necessary types
    df = pd.read_csv(filename, sep=r'\s*,\s*', engine='python', na_values=[""],
        dtype={"race_type": "category", "race_number": "Int64", 
        "race_name": "string", "race_venue": "string"}, 
        parse_dates=[4], date_parser=pd.to_datetime)

    # handle duplicated rows
    # TODO: choose to select one of the row instead
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
    date_today = dt.date.today()

    selected_data = df[(df.race_start_time.dt.date == date_today)
                        & (df.race_start_time > dt.datetime.now())]

    # sort the races
    selected_data = selected_data.sort_values(by=["race_start_time", "race_number", "race_name"])

    # require only the time
    selected_data["race_start_time"] = selected_data.race_start_time.dt.strftime("%H.%M")

    # construct the race info based on race_number and race_name
    race_info = []
    for num, name in zip(selected_data["race_number"], selected_data["race_name"]):
        if pd.isna(name):
            race_info.append(f"Race {num}")
            continue

        if pd.isna(num):
            race_info.append(f"{name}")
        else:
            race_info.append(f"Race {num} - {name}")

    selected_data["race_info"] = race_info

    return selected_data[["race_type", "race_venue", "race_start_time", "race_info"]]

def extract_next_to_jump(df):
    '''
        Input - cleaned dataframe of next-to-jump races consisting of:
                1. race_type
                2. race_venue
                3. race_start_time
                4. race_info    
        
        Output - list of dictionaries with the input and its value
            e.g [ {race_type: 1, race_venue: "Melbourne", ... }, ...]
    '''
    return df.to_dict('records')

df = clean_data("data1.csv")
print(extract_next_to_jump(df))