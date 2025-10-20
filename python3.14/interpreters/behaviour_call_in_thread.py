from time import sleep
from concurrent import interpreters

interp = interpreters.create()

def run():
    from time import sleep
    sleep(5)
    print("Hello from new interpreter")

print("Executing run()")
t = interp.call_in_thread(run)

sleep(5)
print("Hello from original interpreter")

t.join()
