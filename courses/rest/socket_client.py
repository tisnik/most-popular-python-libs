import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

connection.connect(("127.0.0.1", 5555))

message = b"Hello world\r\n"

connection.send(message)
print("Sent")

exit()
