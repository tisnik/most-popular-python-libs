import typing
import strawberry


def get_books_for_author(author: str):
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
    return [book for book in books if book.author == author]


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books_for_author)


schema = strawberry.Schema(query=Query)
