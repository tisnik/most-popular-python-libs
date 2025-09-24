
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


def get_books_for_author_with_name(author_name: str | None = None) -> list[Book]:
    if author_name is None:
        return [Book(title=record[0]) for record in database]
    return [Book(title=record[0]) for record in database if record[1] == author_name]


def get_books_for_author(root: "Author") -> list[Book]:
    return get_books_for_author_with_name(None if root is None else root.name)


@strawberry.type
class Author:
    name: str
    books: list[Book] = strawberry.field(resolver=get_books_for_author)


def get_authors(root) -> list[Author]:
    return [Author(name=record[1]) for record in database]


@strawberry.type
class Query:
    authors: list[Author] = strawberry.field(resolver=get_authors)
    books: list[Book] = strawberry.field(resolver=get_books_for_author_with_name)


schema = strawberry.Schema(query=Query)
