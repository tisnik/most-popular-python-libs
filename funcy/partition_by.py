from funcy import partition_by

values = range(20)

sequences = partition_by(lambda x : x // 5, values)

for sequence in sequences:
    print(list(sequence))
