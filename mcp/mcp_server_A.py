"""MCP server se zdrojem,  dynamickým zdrojem a definicí nástroje (tool)."""

from time import sleep

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")

SLEEP_AMOUNT=0.5


@mcp.tool()
def factorial(n: int) -> int:
    """Výpočet faktoriálu ve smyčce."""
    print("Factorial computation started")
    f = 1
    for x in range(1, n + 1):
        f *= x
    sleep(SLEEP_AMOUNT)
    print("Factorial computation finished")
    return f


@mcp.resource("pozdrav://")
def pozdrav1() -> str:
    """Odpověď s pozdravem."""
    print("Resource preparation started")
    sleep(SLEEP_AMOUNT)
    print("Resource preparation finished")
    return "Hello, dear client!"


@mcp.resource("pozdrav://{name}")
def pozdrav2(name: str) -> str:
    """Odpověď s osobním pozdravem."""
    print("Resource preparation started")
    sleep(SLEEP_AMOUNT)
    print("Resource preparation finished")
    return f"Hello, {name}!"


# přímé spuštění serveru v režimu SSE (Server-Sent Events)
if __name__ == "__main__":
    mcp.run(transport="sse")
