#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Simplest Flask-based application."""

from flask import Flask

from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def hello_world():
    """Implement handler for the / endpoint."""
    return "Hello, World!\n"
