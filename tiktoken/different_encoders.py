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


def compare_encodings(example_string: str) -> None:
    print(f'\nExample string: "{example_string}"')

    for encoding_name in ["o200k_base", "r50k_base", "p50k_base", "cl100k_base"]:
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(example_string)
        num_tokens = len(tokens)
        bytes = [encoding.decode_single_token_bytes(token) for token in tokens]

        print()
        print(f"{encoding_name}: {num_tokens} tokens")
        print(f"token integers: {tokens}")
        print(f"token bytes: {bytes}")

    print()


compare_encodings("The quick brown fox jumps over the lazy dog.")

compare_encodings("firefox")

