from utils.tui import *

def main():
    title()
    operation = select_opertation()
    if operation == 0:
        select_scale()
    elif operation == 1:
        print("wip")

if __name__ == "__main__":
    main()