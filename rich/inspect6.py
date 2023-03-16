#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from rich import inspect
from queue import Queue

q = Queue()

q.put(42)
q.put(3.14)
q.put(True)
q.put(None)

inspect(q, methods=True, private=True)
