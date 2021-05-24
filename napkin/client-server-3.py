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

import napkin


@napkin.seq_diagram()
def client_server_2(c):
    client = c.object('Client')
    server = c.object('Server')

    with client:
        with server.SYN():
            with client.SYN_ACK():
                server.ACK()
