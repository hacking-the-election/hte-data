
import json
with open('geodata.json', 'r') as f1, open('election_data.tab', 'r') as f2:
    geodata = json.load(f1)
    election_data = f2.read()

    election_data = [thing.split('\t') for thing in election_data.split('\n')]
    pop = {}
    for precinct in election_data:
        pop[precinct[0]] = precinct[3]

for precinct in geodata["features"]:
    precinct["properties"]["POP_TOT_00"] = pop[precinct["properties"]["GEOID10"]]

with open('geodata_new.json', 'w') as f:
    json.dump(geodata, f, indent=0)