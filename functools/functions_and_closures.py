def foo():

   def bar():
       print("original BAR")

   def other_bar():
       print("modified BAR")

   def baz(modify):
       nonlocal bar
       if modify:
           bar = other_bar
       return bar
   return baz

x = foo()

print(x)
x(False)()
x(True)()
