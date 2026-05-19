try:
    1/0
except Exception as e:
    print(e)

try:
    -1/0
except Exception as e:
    print(e)

try:
    0/0
except Exception as e:
    print(e)
