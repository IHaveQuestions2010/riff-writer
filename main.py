from utils.variables import selected_scale, string_names
from utils.music_theory import generate_fretboard_for_scale

def main():
    scale = selected_scale
    notes, notes_in_scale, frets = generate_fretboard_for_scale(scale, string_names)
    print(notes,notes_in_scale, frets)

if __name__ == "__main__":
    main()