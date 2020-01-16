import json


with open ('.\data\conflict_data_full_lined.json') as json_file:
    data = json.load(json_file)

    # Which attribues do I want and need?:
    # Id, 
    # Country, 
    # year, 
    # best, 
    # active_year, 
    # type_of_violence, 
    # source_article, 
    # event_clarity

with open('israel_data.csv', 'w', encoding='utf8') as file:
        #for loop to get the whole entry
    for entry in data:
        file.write(f'{entry["id"]},{entry["country"]},{entry["year"]},{entry["best"]},{entry["active_year"]}, {entry["type_of_violence"]},{entry["event_clarity"]},{entry["source_article"]}\n')

