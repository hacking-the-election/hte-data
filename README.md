# data
A repository of all data used and created in the hacking-the-election project

### Contents
- `/raw`: Contains unaltered source data for the project. Each state contains a compressed data.zip file
     - `/raw/*/data.zip`:
          - `district.json`: geojson of all the districts in a state
          - `election_data.tab`: tsv of the election data
          - `geodata.json`: geojson for the precincts in a state
- `/bin`: Binary serialized objects
      - cpp: C++ parseable objects (`boost_serialization`)
      - python: `pickled` objects parseable in python.

## Contributing
Due to the unstable nature of this repository, we aren't looking for pull requests.
