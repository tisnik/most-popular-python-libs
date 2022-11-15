from rich import inspect
from queue import Queue

q = Queue()

q.put(42)
q.put(3.14)
q.put(True)
q.put(None)

inspect(q, methods=True, private=True)
