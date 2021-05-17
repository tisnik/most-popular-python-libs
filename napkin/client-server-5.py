import napkin


@napkin.seq_diagram()
def client_server_5(c):
    client = c.object('Client')
    server = c.object('Server')

    with client:
        with server.SYN():
            c.ret("SYN_ACK")
        server.ACK()
