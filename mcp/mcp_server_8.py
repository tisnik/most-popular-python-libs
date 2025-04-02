"""Jednoduchý MCP server s jediným definovaným dynamickým zdrojem."""

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")


@mcp.resource("author://{name}-{surname}", mime_type="application/json")
def author(name: str, surname: str) -> list:
    """Knihy od vybraného autora."""
    return [
        {"name": name, "surname": surname, "title": "Foo", "year": 1900},
        {"name": name, "surname": surname, "title": "Bar", "year": 2005},
        {"name": name, "surname": surname, "title": "Baz", "year": 2025},
    ]


# přímé spuštění serveru v režimu SSE (Server-Sent Events)
if __name__ == "__main__":
    mcp.run(transport="sse")
