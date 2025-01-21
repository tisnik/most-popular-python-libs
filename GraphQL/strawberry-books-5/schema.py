import typing
from typing import Optional
import strawberry


database = (
    ("Dune", "Frank Herbert"),
    ("Dune Messiah", "Frank Herbert"),
    ("Mythago Wood", "Robert Holdstock"),
    ("Merlin's Wood", "Robert Holdstock"),
    ("Lavondyss", "Robert Holdstock"),
)


def get_author_for_book(root: "Book") -> "Author":
    for record in database:
        if record[0] == root.title:
            return Author(name=record[1])
    return None


@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root: "Author") -> list[Book]:
    if root is None:
        return [Book(title=record[0]) for record in database]
    return [Book(title=record[0]) for record in database if record[1] == root.name]


@strawberry.type
class Author:
    name: str
    books: list[Book] = strawberry.field(resolver=get_books_for_author)


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books_for_author)


schema = strawberry.Schema(query=Query)
