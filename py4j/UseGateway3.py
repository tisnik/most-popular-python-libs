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

gateway1 = JavaGateway(gateway_parameters=GatewayParameters(port=20001))
gateway2 = JavaGateway(gateway_parameters=GatewayParameters(port=20002))

message = gateway1.entry_point.getMessage()
print(message)

message = gateway2.entry_point.getMessage()
print(message)

input("Press Enter to continue...")
