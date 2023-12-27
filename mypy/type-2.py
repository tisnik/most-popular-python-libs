type ID = int
type Name = str
type Surname = str

type User = (ID, Name, Surname)

u1:User = (42, "Linus", "Torvalds")
print(u1)
