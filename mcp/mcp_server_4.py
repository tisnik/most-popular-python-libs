"""Jednoduchý MCP server s jediným definovaným dynamickým zdrojem."""

import os
from datetime import datetime

from mcp.server.fastmcp import FastMCP

# konstrukce serveru
mcp = FastMCP("Test")

pid = os.getpid()

# při každém spuštění serveru se vytvoří nový soubor
with open(f"{pid}.txt", "w") as fout:
    fout.write(str(datetime.now()))


@mcp.resource("pozdrav://")
def pozdrav() -> str:
    """Odpověď s pozdravem."""
    return "Hello, dear client"
