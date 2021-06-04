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

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=20001))

message = gateway.entry_point.getMessage()
print(message)

print(gateway.entry_point.add(10, 20))
print(gateway.entry_point.fadd(10.0, 20.0))

aString = gateway.entry_point.sadd("foo", "bar")
print(aString)
print(type(aString))
print()

aList = gateway.entry_point.aList("first", "second")
print(aList)
print(type(aList))
print()

aMap = gateway.entry_point.aMap("key", "value")
print(aMap)
print(type(aMap))
print()

input("Press Enter to continue...")
