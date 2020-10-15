#!/usr/bin/env python3
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

import requests
import json


def set_cookie(session, name, value):
    # adresa s testovaci REST API sluzbou
    URL = "https://httpbin.org/cookies/set/{name}/{value}".format(name=name, value=value)

    # hlavicka posilana v dotazu
    headers = {'accept': 'application/json'}

    # poslani HTTP dotazu typu GET
    return session.get(URL, headers=headers)


def delete_cookie(session, name):
    # adresa s testovaci REST API sluzbou
    URL = "https://httpbin.org/cookies/delete?{name}=".format(name=name)

    # hlavicka posilana v dotazu
    headers = {'accept': 'application/json'}

    # poslani HTTP dotazu typu GET
    return session.get(URL, headers=headers)


def print_response(response):
    # precteni hlavicek
    headers = response.headers

    print("-" * 60)

    # vypis hlavicek
    print("Headers:")

    for header_name, header_value in headers.items():
        print("{:40s} {}".format(header_name, header_value))

    print("-" * 60)

    print("Content:")

    # zpracovani odpovedi, ktera prisla ve formatu JSON
    data = response.text

    # zpracovani odpovedi, ktera prisla ve formatu JSON
    data = response.json()

    print(json.dumps(data, indent=4, sort_keys=True))

    print("-" * 60)


def print_session_cookies(session):
    cookies = session.cookies
    print("Session cookies:")

    for cookie_name, cookie_value in cookies.items():
        print("{:40s} {}".format(cookie_name, cookie_value))

    print("-" * 60)


session = requests.Session()

print("*** set cookie 'foo'=6 ***")
response = set_cookie(session, "foo", "6")
print_response(response)
print_session_cookies(session)
print()

print("*** set cookie 'bar'=7 ***")
response = set_cookie(session, "bar", "7")
print_response(response)
print_session_cookies(session)
print()

print("*** set cookie 'foo'=42 ***")
response = set_cookie(session, "foo", "42")
print_response(response)
print_session_cookies(session)
print()

print("*** delete cookie 'foo' ***")
response = delete_cookie(session, "foo")
print_response(response)
print_session_cookies(session)
print()

print("*** delete cookie 'baz' ***")
response = delete_cookie(session, "baz")
print_response(response)
print_session_cookies(session)
print()

