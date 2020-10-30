# Python script to convert a csv file to json file
import json
import csv

# Open and read the csv file; skip the header row
with open("Cars.csv", "r") as cfile:
    reader = csv.reader(cfile)
    next(reader)
    # Create the dictionary named data
    data = {"Cars": []}
    # Traverse the csv file and save the data in "data"
    for row in reader:
        data["Cars"].append({"Number": row[0], "Company": row[1], "Model": row[2]})

# Write data to json file
with open("Cars.json", "w") as jfile:
    json.dump(data, jfile, indent=4)