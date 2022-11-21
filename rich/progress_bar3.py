from rich.progress import Progress
import time

with Progress() as progress_bars:

    task1 = progress_bars.add_task("[blue]Task #1...", total=100)
    task2 = progress_bars.add_task("[yellow]Task #2...", total=100)

    while not progress_bars.finished:
        progress_bars.update(task1, advance=0.3)
        progress_bars.update(task2, advance=0.2)
        time.sleep(0.01)
