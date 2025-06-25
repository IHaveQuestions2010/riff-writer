from rich.console import Console
from rich.text import Text
import readchar
import sys

console = Console()

scale_names = ["C", "G", "D", "A", "E", "B", "F#", "C#", 
               "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]
selected_index = 0

def render_scale_line(scale_names, selected_index):
    text = Text()
    for i, name in enumerate(scale_names):
        if i == selected_index:
            text.append(name + " ", style="underline bold yellow")
        else:
            text.append(name + " ", style="dim")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    console.print(text, end="")

while True:
    render_scale_line(scale_names, selected_index)
    key = readchar.readkey()
    if key == readchar.key.RIGHT:
        selected_index = (selected_index + 1) % len(scale_names)
    elif key == readchar.key.LEFT:
        selected_index = (selected_index - 1) % len(scale_names)
    elif key == readchar.key.ENTER:
        break

selected_scale = scale_names[selected_index]
print("")
console.print(f"Selected scale: [bold green]{selected_scale}[/]")