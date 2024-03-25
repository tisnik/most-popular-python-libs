x = 1
y = 2
z = 3

def add_globals():
    global x, y, z
    z = x + y

add_globals(1, 2)
print(z)
