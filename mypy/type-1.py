#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

type Names = List[str]
type Scores = List[int]


def print_score_table(names: Names, scores: Scores) -> None:
    for name, score in zip(names, scores):
        print(name, score)


print_score_table(["aa", "bb"], [1, 2])
