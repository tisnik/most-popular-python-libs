"""MCP server se zdrojem s obrázkem."""

from PIL import Image as PILImage
from PIL import ImageDraw

from mcp.server.fastmcp import FastMCP, Image

# konstrukce serveru
mcp = FastMCP("Test")


#@mcp.resource("house://", mime_type="image/png")
@mcp.tool()
def house() -> Image:
    """Vrací rastrový obrázek."""
    # vytvoření prázdného obrázku
    image = PILImage.new("1", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(image)

    endpoints = [
        100,
        500,
        400,
        200,
        100,
        200,
        250,
        50,
        400,
        200,
        400,
        500,
        100,
        200,
        100,
        500,
        400,
        500,
    ]

    draw.line(endpoints, fill=255)

    return Image(data=image.tobytes(), format="png")


# přímé spuštění serveru v režimu SSE (Server-Sent Events)
if __name__ == "__main__":
    mcp.run(transport="sse")
