"""Jednoduchý MCP server s jediným definovaným dynamickým zdrojem."""

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")


@mcp.resource("pozdrav://{name}")
def pozdrav(name: str) -> str:
    """Odpověď s osobním pozdravem."""
    return f"Hello, {name}"
