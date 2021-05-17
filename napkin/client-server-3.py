import napkin


@napkin.seq_diagram()
def client_server_2(c):
    client = c.object('Client')
    server = c.object('Server')

    with client:
        with server.SYN():
            with client.SYN_ACK():
                server.ACK()
