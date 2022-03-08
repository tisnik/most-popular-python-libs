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
def request_response_3(c):
    client = c.object("Client")
    frontend = c.object('"Front end"')
    backend = c.object('"Back end"')

    with client:
        with frontend.request("login='foo'", "password='bar'"):
            with backend.try_login("'foo'", "'bar'"):
                c.ret("login ok")
            c.ret("login ok")

    with c.loop():
        with client:
            with frontend.request("login='foo'", "password='xyzzy'"):
                with backend.try_login("'foo'", "'bar'"):
                    c.ret("login failed")
                c.ret("login failed")
