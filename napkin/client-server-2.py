import napkin


@napkin.seq_diagram()
def client_server_2(c):
    client = c.object('Client')
    server = c.object('Server')

    with client:
        server.SYN()

    with server:
        client.SYN_ACK()

    with client:
        server.ACK()
