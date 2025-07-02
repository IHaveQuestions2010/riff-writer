from utils.tui import *

def main():
    title()
    operation = list_options(["Generate a tab"])
    if operation == 0:
        list_options([display_note(n) for n in all_notes])
    elif operation == 1:
        print("wip")

if __name__ == "__main__":
    main()