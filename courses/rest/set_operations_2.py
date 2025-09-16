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
