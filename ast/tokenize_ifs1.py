#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import tokenize

with tokenize.open("ifs1.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print(token)
