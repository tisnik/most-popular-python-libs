from rich.console import Console
from rich.table import Table

table = Table(title="Barvové modely")

table.add_column("Zkratka")
table.add_column("Význam")

table.add_row("RGB", "Red Green Blue")
table.add_row("CMYK", "Cyan Magenta Yellow blacK")
table.add_row("HSL", "Hue Saturation Lightness")
table.add_row("HSV", "Hue Saturation Value")

console = Console()
console.print(table)
