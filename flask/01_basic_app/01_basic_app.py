#!/usr/bin/env python
# vim: set fileencoding=utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!\n'
