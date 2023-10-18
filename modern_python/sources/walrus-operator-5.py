values = (1, 2, 3, 4, 5)

result = {
        "count": (count := len(values)),
        "sum": (summ := sum(values)),
        "mean": summ/count
        }

print(result)
