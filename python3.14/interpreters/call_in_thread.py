from concurrent import interpreters

interp = interpreters.create()

def run():
    print("Hello from new interpreter")

print("Executing run()")
t = interp.call_in_thread(run)

print("Hello from original interpreter")

t.join()
