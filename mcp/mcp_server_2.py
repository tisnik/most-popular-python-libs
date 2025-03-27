from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test")


@mcp.resource("pozdrav://{name}")
def pozdrav(name: str) -> str:
    """Odpoveď s osobním pozdravem."""
    return f"Hello, {name}"
