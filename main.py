selected_scale = "C"

base_tab = """e|---------------------------------------------------------------|
B|---------------------------------------------------------------|
G|---------------------------------------------------------------|
D|---------------------------------------------------------------|
A|---------------------------------------------------------------|
E|---------------------------------------------------------------|"""

ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

MAJOR_SCALES = {
    "C": ["C", "D", "E", "F", "G", "A", "B"], # All natural

    "G": ["G", "A", "B", "C", "D", "E", "F#"], # One sharp
    "D": ["D", "E", "F#", "G", "A", "B", "C#"], # Two sharps
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"], # Three sharps
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"], # Four sharps
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"], # Five sharps
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"], # Six sharps
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"], # Seven sharps

    "F": ["F", "G", "A", "Bb", "C", "D", "E", "F"], # One flat   
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"], # Two flats
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"], # Three flats
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"], # Four flats
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], # Five flats
    "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"], # Six flats
    "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"] # Seven flats
}

# Probably won't be used
'''
MINOR_SCALES = {
    "Am": MAJOR_SCALES["C"], # All naturals

    "Em": MAJOR_SCALES["G"], # One sharp
    "Bm": MAJOR_SCALES["D"], # Two sharps
    "F#m": MAJOR_SCALES["A"], # Three sharps
    "C#m": MAJOR_SCALES["E"], # Four sharps
    "G#m": MAJOR_SCALES["B"], # Five sharps
    "D#m": MAJOR_SCALES["F#"], # Six sharps
    "A#m": MAJOR_SCALES["C#"], # Seven sharps

    "Dm": MAJOR_SCALES["F"], # One flat
    "Gm": MAJOR_SCALES["Bb"], # Two flats
    "Cm": MAJOR_SCALES["Eb"], # Three flats
    "Fm": MAJOR_SCALES["Ab"], # Four flats
    "Bbm": MAJOR_SCALES["Db"], # Five flats
    "Ebm": MAJOR_SCALES["Gb"], # Six flats
    "Abm": MAJOR_SCALES["Cb"] # Seven flats
}
'''

def get_notes_on_string(open_note):
    """Return the 12 notes on a string starting from its open note."""
    offset = ALL_NOTES.index(open_note)
    return [ALL_NOTES[(i + offset) % 12] for i in range(12)]

def is_note_in_scale(scale, note):
    """Check if a note is in the given major scale."""
    return note in MAJOR_SCALES[scale]

STRING_NAMES = ["E", "B", "G", "D", "A"]

notes_per_string = [get_notes_on_string(name) for name in STRING_NAMES]
notes_on_strings_in_scale = [[] for _ in STRING_NAMES]
positions_on_strings_in_scale = [[] for _ in STRING_NAMES]

for string_idx, string_notes in enumerate(notes_per_string):
    for fret, note in enumerate(string_notes):
        if is_note_in_scale(selected_scale, note):
            notes_on_strings_in_scale[string_idx].append(note)
            positions_on_strings_in_scale[string_idx].append(fret)

for string_idx, string_notes in enumerate(notes_per_string):
    for fret, note in enumerate(string_notes):
        if note in notes_on_strings_in_scale[string_idx]:
            print(f"{fret}-", end="")
        else:
            print("x-", end="")
    print("")
