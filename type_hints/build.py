#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Simple preprocessor for Markdown files that handles @ character as include statement."""

import os

input_file = "type_hints_in.md"
output_file = "type_hints.md"

source_prefix = (
    "https://github.com/tisnik/most-popular-python-libs/blob/master/type_hints/"
)

source_directory = "examples/"

with open(input_file, "r") as fin:
    with open(output_file, "w") as fout:
        for line in fin.readlines():
            # handle @ character at the beginning of line as include statement
            if line[0:2] == "@ ":
                # retrieve file name of file to be included
                include = line[2:].strip()
                full_name = source_directory + include
                #print("including:", full_name)

                # perform the inclusion within ```python block
                fout.write("```python\n")
                try:
                    with open(full_name, "r") as inc:
                        included = inc.read()
                        fout.write(included)
                except Exception as e:
                    print(e)
                fout.write("```\n\n")
                #fout.write("[Zdrojový kód tohoto příkladu]({}/{})".format(source_prefix, include))
                #fout.write("\n")
            # other lines are to be output in its original form
            else:
                fout.write(line)

