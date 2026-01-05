from kivy.uix.label import Label

for item in vars(Label):
    if item[0] != "_":
        print(item)

print("-"*50)

for item in dir(Label):
    if item not in vars(Label):
        if item[0] != "_":
            print(item)
