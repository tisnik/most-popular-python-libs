type Names = List[str]
type Scores = List[int]


def print_score_table(names: Names, scores: Scores) -> None:
    for name, score in zip(names, scores):
        print(name, score)


print_score_table(["aa", "bb"], [1, 2])
