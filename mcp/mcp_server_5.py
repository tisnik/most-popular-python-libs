"""MCP server se zdrojem,  dynamickým zdrojem a definicí nástroje (tool)."""

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")


@mcp.tool()
def factorial(n: int) -> int:
    """Výpočet faktoriálu ve smyčce."""
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


@mcp.resource("pozdrav://")
def pozdrav1() -> str:
    """Odpověď s pozdravem."""
    return "Hello, dear client"


@mcp.resource("pozdrav://{name}")
def pozdrav2(name: str) -> str:
    """Odpověď s osobním pozdravem."""
    return f"Hello, {name}"


# přímé spuštění serveru v režimu STDIO
if __name__ == "__main__":
    mcp.run()
