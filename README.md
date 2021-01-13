# API-for-Next-to-Jump
API to return a list of "Next-to-Jump" races. 

## Definition of "Next-to-Jump":
The remaining races as of today. <br />
Races that are in the past are not returned. <br />

## Input:
CSV file with the specified headers as below. <br />

## Output:
List of dictionaries containing race type, race info, race venue and the race start time, <br />
sorted ascending in the importance as below: <br />
1. Race start time
2. Race number
3. Race name


## Using the API:
- System requirements: 
    1.  Python 3.6 and above
    2.  Pip 19.x and above
<br />
- Dependencies are recorded in requirements.txt. <br />
    To install dependencies, execute from command line: <br />
        ```
        pip install -r requirements.txt
        ```
<br />
- Import module in a Python script using 
```
from api_utils import extract_next_to_jump
```
and run
```
output = extract_next_to_jump(filename)
```
where the data structure is returned in output.

## DEMO:
- To view the returned data structure in terminal, execute from command line:<br />
        ```
        python3 next_to_jump.py <filename> 
        ```
<br />
- To access the output in text file, execute from command line:<br />
        ```
        python3 next_to_jump.py <filename> > <output>.txt
        ```

## Assumptions:
API takes in CSV files with HEADERS of order: <br />
1. race_type
2. race_number
3. race_name
4. race_venue
5. race_start_time

### Mandatory attributes & types:
race_type       : categorical <br />
race_venue      : string <br />
race_start_time : datetime object, (format yyyy-MM-dd HH:mm:ss) <br />

### Optional attributes & types:
(At least one must be present) <br />
race_number     : integer <br />
race_name       : string <br />

### Removes:
- Duplicated rows (retains the first occurrence)
- Rows containing empty entries of race_type, race_venue, race_startime
- Rows containing empty entries of BOTH race_number and race_name