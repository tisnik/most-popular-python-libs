#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from pywebio import *
from pywebio.input import *
from pywebio.output import *


def main():
    put_info("Výsledky měření senzorů")


start_server(main, port=8080, debug=True)
