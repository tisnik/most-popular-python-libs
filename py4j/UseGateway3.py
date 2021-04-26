from py4j.java_gateway import JavaGateway, GatewayParameters

gateway1 = JavaGateway(gateway_parameters=GatewayParameters(port=20001))
gateway2 = JavaGateway(gateway_parameters=GatewayParameters(port=20002))

message = gateway1.entry_point.getMessage()
print(message)

message = gateway2.entry_point.getMessage()
print(message)

input("Press Enter to continue...")
