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
