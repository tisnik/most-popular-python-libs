from rich.progress import track
from time import sleep


def process_data():
    sleep(0.02)


for _ in track(range(100), description="[green]Processing data"):
    process_data()
