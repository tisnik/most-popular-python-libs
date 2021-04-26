from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

message = gateway.entry_point.getMessage()
print(message)

input("Press Enter to continue...")
