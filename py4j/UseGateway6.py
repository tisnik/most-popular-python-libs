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

from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway()

# zavolání konstruktoru Javovské třídy
o = gateway.jvm.java.lang.Object()
print(o)

# zavolání metody objektu
print(o.toString())

print()

# zavolání statické metody třídy
r = gateway.jvm.java.lang.Math.random()
print(r)
print()

# použití datové struktury ArrayList z Javy
lst = gateway.jvm.java.util.ArrayList()

lst.append("first")
lst.append("second")

for i in range(1, 11):
    lst.append(i)

print(lst)
print()

# přístup k atributu
Pi = gateway.jvm.java.lang.Math.PI
e = gateway.jvm.java.lang.Math.E
print(Pi)
print(e)
print()

# import Javovské třídy
from py4j.java_gateway import java_import

java_import(gateway.jvm, "java.util.*")

# rozdílné oproti předchozímu příkladu
lst = gateway.jvm.ArrayList()

lst.append("first")
lst.append("second")

for i in range(1, 11):
    lst.append(i)

print(lst)
print()


# vytvoření jednorozměrného pole
string_class = gateway.jvm.String
string_array = gateway.new_array(string_class, 5)
string_array[0] = "first"
string_array[1] = "second"
print(string_array[0])
print(string_array[1])
