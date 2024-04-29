from json import load
from box import Box

with open("openapi.json") as fin:
    j = load(fin)

print(j)
print()

b = Box(j, box_dots=True)

print(b["info"]["license"]["name"])
print(b.info.license.name)
print(b["info.license.name"])
