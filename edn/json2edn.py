#!/usr/bin/env python3

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# Converts structured data from JSON format into EDN format.

import sys
import json
import edn_format

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  json2edn.py input_file.csv")
    print("Example:")
    print("  json2edn.py report.csv")
    sys.exit(1)

# First command line argument should contain name of input JSON file.
input_json = sys.argv[1]

# Try to open the JSON file specified.
with open(input_json) as json_input:
    # open the JSON file and parse it
    payload = json.load(json_input)
    # dump the parsed data structure into EDN format
    print(edn_format.dumps(payload))
