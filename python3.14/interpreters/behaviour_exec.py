from time import sleep
from concurrent import interpreters

interp = interpreters.create()

def run():
    from time import sleep
    sleep(5)
    print("Hello from new interpreter")

print("Executing run()")
interp.exec(run)

sleep(5)
print("Hello from the original interpreter")
