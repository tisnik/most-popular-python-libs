#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

import pywebio.output as out

out.put_table(
    [
        ["Language", "Ratings"],
        ["C", "15.95"],
        ["Java", "13.48"],
        ["Python", "10.47"],
        ["C++", "7.11"],
        ["C#", "4.58"],
        ["Visual Basic", "4.12"],
        ["JavaScript", "2.54"],
        ["PHP", "2.49"],
        ["R", "2.37"],
        ["SQL", "1.76"],
        ["Go", "1.46"],
        ["Swift", "1.38"],
        ["Perl", "1.30"],
        ["Assembly language", "1.30"],
        ["Ruby", "1.24"],
        ["MATLAB", "1.10"],
        ["Groovy", "0.99"],
        ["Rust", "0.92"],
        ["Objective-C", "0.85"],
        ["Dart", "0.77"],
    ]
)
