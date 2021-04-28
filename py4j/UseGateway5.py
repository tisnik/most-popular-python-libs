from py4j.java_gateway import JavaGateway, GatewayParameters
import pprint

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=20001))

m = gateway.entry_point.getMap()
print("Original map:")
pprint.pprint(m)
print()

m["foo"] = "bar"
print("Updated map:")
pprint.pprint(m)
print()

print("Java side...")
gateway.entry_point.printMap()
print()

m["bar"] = "baz"
del m["foo"]
print("Updated map:")
pprint.pprint(m)
print()

print("Java side...")
gateway.entry_point.printMap()
print()

input("Press Enter to continue...")
