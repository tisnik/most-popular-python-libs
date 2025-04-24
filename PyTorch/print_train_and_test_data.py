# trénovací a testovací data
from compute_train_and_test_data import compute_train_and_test_data

train_data, test_data = compute_train_and_test_data()

print(train_data.X)
print(train_data.y)

print()
print(test_data.X)
print(test_data.y)

