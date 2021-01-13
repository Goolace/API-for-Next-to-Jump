import pandas as pd
import numpy as np
import datetime as dt

# TODO: pretty print
def pretty_print_tabular():
    raise NotImplementedError
    return

def _select_valid_race(df):
    '''
        Input   - pandas dataframe
        Output  - The index of rows containing neither race number nor race name
    '''
    row_index, _ = np.where(pd.isnull(df))

    # TODO: assert col_index is in range 1-2
    curr = -1
    index = []
    for item in row_index:
        if item == curr:
            index.append(item)
        curr = item
    
    return index

def _concat_race_info(df):
    '''
    Function concatenates race_venue and race_time into race_info for front-end display.
        Input   -  pandas dataframe of next-to-jump races
        Output  -  a list containing the race info concatenated as below from race_venue and race_time:

            if race_number is not present, print:
                <race_name>
            if race_name is not present, print:
                Race <race_number>
            if both are present, print:
                Race <race_number> - <race_name>
    '''

    race_info = []
    for num, name in zip(df["race_number"], df["race_name"]):
        if pd.isna(name):
            race_info.append(f"Race {num}")
            continue

        if pd.isna(num):
            race_info.append(f"{name}")
        else:
            race_info.append(f"Race {num} - {name}")
    
    return race_info

def _clean_data(filename):
    '''
        Input   - filename
        Output  - dataframe containing 
        race_type, race_info (race_number and race_name concatenated), race_venue, race_time
    '''

    # Check that CSV is in a required format and enforce the necessary types
    df = pd.read_csv(filename, sep=r'\s*,\s*', engine='python', na_values=[""],
        dtype={"race_type": "category", "race_number": "Int64", 
        "race_name": "string", "race_venue": "string"}, 
        parse_dates=[4], date_parser=pd.to_datetime)

    # handle duplicated rows
    df = df.drop_duplicates()

    # check mandatory fields
    df.dropna(subset=["race_type", "race_venue", "race_start_time"], inplace=True)

    # remove invalid rows containing neither race number nor race name
    duplicated_index = _select_valid_race(df)
    df.drop(df.index[duplicated_index], inplace=True)

    # select Next-to-jump races for today 
    date_today = dt.date.today()

    selected_data = df[(df.race_start_time.dt.date == date_today)
                        & (df.race_start_time > dt.datetime.now())]

    # sort the races
    selected_data = selected_data.sort_values(by=["race_start_time", "race_number", "race_name"])

    # require only the time
    selected_data["race_start_time"] = selected_data.race_start_time.dt.strftime("%H.%M")

    # construct the race info based on race_number and race_name
    selected_data["race_info"] = _concat_race_info(selected_data)

    return selected_data[["race_type", "race_venue", "race_start_time", "race_info"]]

def extract_next_to_jump(filename):
    '''
        Input - filename of CSV data
        
        Output - list of dictionaries with the input and its value
            e.g [ {race_type: 1, race_venue: "Melbourne", ... }, ...]
    '''

    df = _clean_data(filename)
    return df.to_dict('records')