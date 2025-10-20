from concurrent import interpreters

interp = interpreters.create()

x = []

def run():
    x.append("*")

print("x=", x)

run()
print("x=", x)

t = interp.call_in_thread(run)
t.join()

print("x=", x)
