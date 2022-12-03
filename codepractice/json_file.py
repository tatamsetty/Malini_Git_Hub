import json


# load file into python object with load method

with open('C:/Malini/Precision/codepractice/us_states.json') as f:
    data = json.load(f)
    
for state in data:
    print(state['name'])


# Write to JSON file with dump method
for state in data:
    del state['abbreviation']

with open('C:/Malini/Precision/codepractice/us_states_new.json', 'w') as f:
  json.dump(data,f,indent=2)
    
