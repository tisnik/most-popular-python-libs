import napkin


@napkin.seq_diagram()
def request_response_3(c):
    client = c.object('Client')
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
