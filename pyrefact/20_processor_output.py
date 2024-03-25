#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Simple preprocessor for Markdown files that handles @ character as include statement."""

INPUT_FILE = "modern_python_input.md"
OUTPUT_FILE = "modern_python.md"


SOURCE_DIRECTORY = "sources/"

with open(INPUT_FILE, "r") as fin:
    with open(OUTPUT_FILE, "w") as fout:
        for line in fin.readlines():
            # handle @ character at the beginning of line as include statement
            if line[0:2] == "@ ":
                # retrieve file name of file to be included
                include = line[2:].strip()
                full_name = SOURCE_DIRECTORY + include
                print("including:", full_name)

                # perform the inclusion within ```python block
                fout.write("```python\n")
                with open(full_name, "r") as inc:
                    included = inc.read()
                fout.write(included)
                fout.write("```\n\n")
                fout.write("[Zdrojový kód příkladu]({}/{})".format(sourSOURCE_PREFIXclude))
                fout.write("\n")
            # other lines are to be output in its original form
            else:
                fout.write(line)
