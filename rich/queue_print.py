from queue import Queue

q = Queue()

q.put(42)
q.put(3.14)
q.put(True)
q.put(None)

print(q)
print(q.__dict__)
