from rich.console import Console
from rich.table import Table

table = Table(title="Barvové modely")

table.add_column("Zkratka")
table.add_column("Význam")
table.add_column("Komponenty")

table.add_row("RGB", "Red Green Blue", "[red]Red [green]Green [blue]Blue")
table.add_row("CMYK", "Cyan Magenta Yellow blacK", "[cyan]Cyan [magenta]Magenta [yellow]Yellow [black]blacK")
table.add_row("HSL", "Hue Saturation Lightness", "")
table.add_row("HSV", "Hue Saturation Value", "")

console = Console()
console.print(table)

