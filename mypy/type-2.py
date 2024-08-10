#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

type ID = int
type Name = str
type Surname = str

type User = (ID, Name, Surname)

u1:User = (42, "Linus", "Torvalds")
print(u1)
