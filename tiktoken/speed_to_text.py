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

from time import perf_counter
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

start_time = perf_counter()

tokens = encoder.encode("The quick brown fox jumps over the lazy dog.")

characters_count = 0
for i in range(100000):
    text = encoder.decode(tokens)
    characters_count += len(text)

end_time = perf_counter()

seconds = end_time-start_time

print("Characters:", characters_count)
print("Time:", seconds, "seconds")

speed = int(characters_count / seconds)
print(speed, "characters per second")
