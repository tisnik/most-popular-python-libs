from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test")


@mcp.resource("pozdrav://")
def pozdrav() -> str:
    """Odpoveď s pozdravem."""
    return f"Hello, dear client"
