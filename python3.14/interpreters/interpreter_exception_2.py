from time import sleep
from concurrent import interpreters

interp = interpreters.create()

def run():
    print("Hello from new interpreter")
    0/0

print("Executing run()")
t = interp.call_in_thread(run)

print("Hello from the original interpreter")

sleep(5)

print("Original interpreter is still alive")

t.join()
