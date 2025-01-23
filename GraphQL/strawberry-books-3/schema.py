#
#  (C) Copyright 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import strawberry


def get_books_for_author(author: str | None = None):
    books = [
        Book(
            title="Dune",
            author="Frank Herbert",
        ),
        Book(
            title="Dune Messiah",
            author="Frank Herbert",
        ),
        Book(
            title="Mythago Wood",
            author="Robert Holdstock",
        ),
        Book(
            title="Merlin's Wood",
            author="Robert Holdstock",
        ),
        Book(
            title="Lavondyss",
            author="Robert Holdstock",
        ),
    ]
    if author is None:
        return books
    return [book for book in books if book.author == author]


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books_for_author)


schema = strawberry.Schema(query=Query)
