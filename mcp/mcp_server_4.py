"""Jednoduchý MCP server s jediným definovaným dynamickým zdrojem."""

import os
from mcp.server.fastmcp import FastMCP
from datetime import datetime

# konstrukce serveru
mcp = FastMCP("Test")

pid = os.getpid()

# při každém spuštění serveru se vytvoří nový soubor
with open(f"{pid}.txt", "w") as fout:
    fout.write(str(datetime.now()))


@mcp.resource("pozdrav://")
def pozdrav() -> str:
    """Odpověď s pozdravem."""
    return f"Hello, dear client"
