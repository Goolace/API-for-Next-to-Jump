# API-for-Next-to-Jump
API to return a list of "Next-to-Jump" races. 

#### Definition of "Next-to-Jump":
The remaining races as of today. <br />
Races that are in the past are not returned. <br />

#### Input:
CSV file with the specified headers as below. <br />

#### Output:
Race type, race info, race venue and the race start time, sorted ascending in the importance as below: <br />
1. Race start time
2. Race number
3. Race name

### Assumptions:
API takes in CSV files with HEADERS of order: <br />
1. race_type
2. race_number
3. race_name
4. race_venue
5. race_start_time

#### Mandatory attributes & types:
race_type       : categorical <br />
race_venue      : string <br />
race_start_time : datetime object, (format yyyy-MM-dd HH:mm:ss) <br />

#### Optional attributes & types:
(At least one must be present) <br />
race_number     : integer <br />
race_name       : string <br />

#### Removes:
- Duplicated rows (retains the first occurrence)
- Rows containing empty entries of race_type, race_venue, race_startime
- Rows containing empty entries of BOTH race_number and race_name