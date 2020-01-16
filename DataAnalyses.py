import data

with open 'conflict_data_full_lined.json' as json_file:
    data = json_file.load()

    total_fatalities = 0
    country = Israel
    year = 2001

    for entry in data:
        if entry[year] == 2001 and entry[] 
