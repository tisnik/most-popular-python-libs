from concurrent import interpreters

interp = interpreters.create()


def run(q):
    print("Hello from new interpreter, waiting for message")
    message = q.get()
    print(f"Message received: '{message}'")


q = interpreters.create_queue()

print("Executing run()")
t = interp.call_in_thread(run, q)

print("Sending message into queue")
q.put("foo")
print("Message sent")

print("Waiting for other interpreter to finish")
t.join()

print("Done")
