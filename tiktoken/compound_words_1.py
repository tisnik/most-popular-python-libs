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

compound_words = (
        "bird",
        "black",
        "blue",
        "blackbird",
        "bluebird",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:12}", tokens)
