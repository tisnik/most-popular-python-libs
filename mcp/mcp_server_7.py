"""Jednoduchý MCP server s jediným definovaným dynamickým zdrojem."""

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")


@mcp.resource("author://{name}-{surname}")
def author(name: str, surname: str) -> list:
    """Knihy od vybraného autora."""
    return [
        {"name": name, "surname": surname, "title": "Foo", "year": 1900},
        {"name": name, "surname": surname, "title": "Bar", "year": 2005},
        {"name": name, "surname": surname, "title": "Baz", "year": 2025},
    ]
