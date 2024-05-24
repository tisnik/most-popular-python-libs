"""Export benchmark results into JSON prepared for further processing."""

import csv
import json

import input_files

results = {}

for input_file in input_files.input_files:
    name = input_file.replace(".times", "")
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        results[name] = []
        for row in csv_reader:
            results[name].append(row)

with open("results.json", "w") as fout:
    json.dump(results, fout, indent=4)
