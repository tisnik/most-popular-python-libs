from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test")


@mcp.tool()
def factorial(n: int) -> int:
    """Výpočet faktoriálu ve smyčce."""
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


@mcp.resource("pozdrav://{name}")
def pozdrav(name: str) -> str:
    """Odpoveď s osobním pozdravem."""
    return f"Hello, {name}"
