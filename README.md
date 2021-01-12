# API-for-Next-to-Jump
API to return a list of "Next to Jump" races. 

#### Input:
CSV file

#### Output:
Race type, race number, race name, venue and the race start time, ordered by race time in ascending order.

### Assumptions:
API takes in CSV files with headers of order: <br />
1. race_type
2. race_number
3. race_name
4. race_venue
5. race_start_time

#### Mandatory attributes & types:
race_type       : categorical <br />
race_venue      : string <br />
race_start_time : string, (format yyyy-MM-dd HH:mm:ss) <br />

#### Optional attributes & types:
(At least one must be present) <br />
race_number     : integer <br />
race_name       : string <br />
