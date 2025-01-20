#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Simple preprocessor for Markdown files that handles @ character as include statement."""

import os

input_list_file = "input_list.txt"
work_file = "go_in.md"
output_file = "go.md"

with open(input_list_file) as input_list:
    lst = input_list.read().replace("\n", " whitespace.md ").replace("# ", "")

command = f"cat {lst} >{work_file}"
os.system(command)

source_prefix = (
    "https://github.com/tisnik/Evoluce_Pythonu_priklady/blob/master/"
)

source_directory = ""

with open(work_file, "r") as fin:
    with open(output_file, "w") as fout:
        for line in fin.readlines():
            # handle @ character at the beginning of line as include statement
            if line[0:2] == "@ ":
                # retrieve file name of file to be included
                include = line[2:].strip()
                full_name = source_directory + include
                #print("including:", full_name)

                # perform the inclusion within ```go block
                fout.write("```go\n")
                try:
                    with open(full_name, "r") as inc:
                        included = inc.read()
                        included = included.replace("\t", "    ")
                        fout.write(included)
                except Exception as e:
                    print(e)
                fout.write("```\n\n\n")
                #fout.write("[Zdrojový kód tohoto příkladu můžete najít na adrese]({}{})".format(source_prefix, include))
                #fout.write("Zdrojový kód tohoto příkladu můžete najít na adrese {}{}".format(source_prefix, include))
                #fout.write("\n")
            # other lines are to be output in its original form
            else:
                fout.write(line)
