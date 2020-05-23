# data
A repository of all data used and created in the hacking-the-election project.

### Contents
- `/raw`: Contains unaltered source data for the project. Each state contains a compressed data.zip file.
     The general format is:
     - `/raw/*/data.zip`:
          - `2016_district.json`: geojson of all the districts in a state, in use during 2016
          - `election_data_and_geodata.json` - combined geodata file with population and election data
- `/bin`: Binary serialized objects
      - cpp: C++ parseable objects (`boost_serialization`)
      - python: `pickled` objects parseable in python.

## Contributing
Due to the unstable nature of this repository, we aren't looking for pull requests.
