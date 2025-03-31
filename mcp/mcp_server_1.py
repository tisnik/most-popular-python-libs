"""Jednoduchý MCP server s jediným definovaným zdrojem."""

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")


@mcp.resource("pozdrav://")
def pozdrav() -> str:
    """Odpověď s pozdravem."""
    return "Hello, dear client"
