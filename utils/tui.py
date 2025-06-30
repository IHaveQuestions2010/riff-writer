from .variables import *
from rich.console import Console
from rich.live import Live
from rich.text import Text
import readchar
import pyfiglet

console = Console()

def title():
    figlet_text = pyfiglet.figlet_format("TABZER", font="standard")
    lines = figlet_text.splitlines()

    if lines and lines[0].startswith(" "):
        lines[0] = lines[0][1:]

    cleaned_text = "\n".join(lines)
    text_block = Text(cleaned_text, style="none")
    console.print(text_block, justify="center")


def render_selector(list_to_render, selected_index=0):
    line = Text(justify="center")
    for i, name in enumerate(list_to_render):
        if i == selected_index:
            line.append(name + " ", style="bold yellow")
        else:
            line.append(name + " ")
    return line

def select_scale():
    notes_displayed = [display_note(n) for n in all_notes]
    selected_index = 0
    with Live(render_selector(notes_displayed, selected_index), refresh_per_second=10, console=console) as live:
        while True:
            key = readchar.readkey()
            if key == readchar.key.RIGHT:
                selected_index = (selected_index + 1) % len(all_notes)
            elif key == readchar.key.LEFT:
                selected_index = (selected_index - 1) % len(all_notes)
            elif key == readchar.key.ENTER:
                break
            live.update(render_selector(notes_displayed, selected_index))
    return selected_index


def select_opertation():
    selected_index = 0
    options = ["Generate a tab", "Edit a tab"]
    with Live(render_selector(options, selected_index), refresh_per_second=10, console=console) as live:
        while True:
            key = readchar.readkey()
            if key == readchar.key.RIGHT:
                selected_index = (selected_index + 1) % len(options)
            elif key == readchar.key.LEFT:
                selected_index = (selected_index -1) % len(options)
            elif key == readchar.key.ENTER:
                break
            live.update(render_selector(options, selected_index))
        return selected_index