#!/usr/bin/env python3

"""Simple tool to convert structured data from EDN format to JSON format."""

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

# Converts structured data from EDN format into JSON format.

import sys
import json
import edn_format

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  edn2json.py input_file.edn")
    print("Example:")
    print("  edn2json.py report.edn")
    sys.exit(1)

# First command line argument should contain name of input EDN file.
filename = sys.argv[1]


# Taken from https://github.com/swaroopch/edn_format/issues/76#issuecomment-749618312
def edn_to_map(x):
    """Convert an edn-like data structure into regular Python map."""
    if isinstance(x, edn_format.ImmutableDict):
        return {edn_to_map(k): edn_to_map(v) for k, v in x.items()}
    elif isinstance(x, edn_format.ImmutableList):
        return [edn_to_map(v) for v in x]
    elif isinstance(x, edn_format.Keyword):
        return x.name
    else:
        return x


# Try to open the EDN file specified.
with open(filename, "r") as edn_input:
    # open the EDN file and parse it
    payload = edn_format.loads(edn_input.read())
    print(json.dumps(edn_to_map(payload), indent=2))
