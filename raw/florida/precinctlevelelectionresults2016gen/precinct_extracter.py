import os

def precinct_extract(file_pattern, attribute):
    files = []
    for file in os.listdir():
        if file[4] == "P":
                files.append(file)
    print(files)
    for file in files:
        with open(file, 'r') as fileobj:
            lines = fileobj.readlines()
        print(len(lines))
        lines = [x for x in lines if x.split('\t')[11] == attribute]
        with open(file, 'w') as fileobj:
            fileobj.writelines(lines)


precinct_extract("asfsa", 'President of the United States')
