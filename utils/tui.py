from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.panel import Panel
import readchar
import pyfiglet

console = Console()
scale_names = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab"]

def title():
    figlet_text = pyfiglet.figlet_format("TABZER", font="standard")
    text_block = Text(figlet_text, style="none")
    console.print(text_block, justify="center")


def render_selector(selected_index):
    line = Text(justify="center")
    for i, name in enumerate(scale_names):
        if i == selected_index:
            line.append(name + " ", style="bold yellow")
        else:
            line.append(name + " ")
    return line

def select_scale():
    selected_index = 0
    with Live(render_selector(selected_index), refresh_per_second=10, console=console) as live:
        while True:
            key = readchar.readkey()
            if key == readchar.key.RIGHT:
                selected_index = (selected_index + 1) % len(scale_names)
            elif key == readchar.key.LEFT:
                selected_index = (selected_index - 1) % len(scale_names)
            elif key == readchar.key.ENTER:
                break
            live.update(render_selector(selected_index))
    return selected_index
title()

