#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = [9906, 1917]
text = encoder.decode(tokens)
print(text)

tokens = [9906, 11, 1917, 0]
text = encoder.decode(tokens)
print(text)

tokens = [9906, 11, 1917, 0, 0, 0, 0]
text = encoder.decode(tokens)
print(text)

tokens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = encoder.decode(tokens)
print(text)

tokens = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
text = encoder.decode(tokens)
print(text)
