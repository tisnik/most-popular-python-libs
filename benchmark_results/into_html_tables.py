"""Writes benchmark results into HTML tables."""

import csv

import input_files

for input_file in input_files.input_files:
    output_file = input_file.replace(".times", ".html")
    print(output_file)
    with open(input_file) as csv_file:
        with open(output_file, "w") as html_file:
            html_file.write("<table>\n")
            html_file.write("<tr><th>Rozlišení</th><th>Čas [s]</th><th>Paměť [kB]</th></tr>\n")
            csv_reader = csv.reader(csv_file, delimiter=" ")
            for row in csv_reader:
                html_file.write(f"<tr><td>{row[0]}&times;{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n")
            html_file.write("</table>\n")
