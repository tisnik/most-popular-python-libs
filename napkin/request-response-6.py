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
def request_response_6(c):
    client = c.object("Client")
    frontend = c.object('"Front end"')
    backend = c.object('"Back end"')

    client.note("Web client")
    frontend.note("Web front end (JS)")
    backend.note("Back end (Go)")

    with c.group("Successful login"):
        with client:
            c.note("Login with proper name and password")
            with frontend.request("login='foo'", "password='bar'").note(
                "Correct password"
            ):
                with backend.try_login("'foo'", "'bar'"):
                    c.ret("login ok")
                c.ret("login ok")

    with c.group("Failed login"):
        with client:
            c.note("Login with improper name and password")
            with frontend.request("login='foo'", "password='xyzzy'").note(
                "Bad password"
            ):
                with c.loop():
                    with backend.try_login("'foo'", "'bar'"):
                        c.ret("login failed")
                    c.ret("login failed")
                    c.note("Trying again ... is meaningless")
