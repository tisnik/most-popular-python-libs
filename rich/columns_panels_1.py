from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


console = Console()

panel1 = Panel("První")
panel2 = Panel("Druhý")
panel3 = Panel("Třetí")

columns = Columns([panel1, panel2, panel3])
console.print(columns)
