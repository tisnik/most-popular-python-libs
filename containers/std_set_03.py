#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

engineers = {"John", "Jane", "Jack", "Janice"}
programmers = {"Jack", "Sam", "Susan", "Janice"}
managers = {"Jane", "Jack", "Susan", "Zack"}

employees = engineers | programmers | managers
engineering_management = engineers & managers
fulltime_management = managers - engineers - programmers

print(engineers)
print(programmers)
print(managers)
print(employees)
print(engineering_management)
print(fulltime_management)
