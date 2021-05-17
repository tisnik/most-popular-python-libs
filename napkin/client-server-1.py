import napkin


@napkin.seq_diagram()
def client_server_1(c):
    client = c.object('Client')
    server = c.object('Server')

    with client:
        server.SYN()
