import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(("0.0.0.0", 5555))
connection.listen(10)

current_connection, address = connection.accept()

data = current_connection.recvfrom(1000)
print("Received")
print(data)
print("Done")

exit()
