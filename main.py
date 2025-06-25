### Variables ###
selected_scale = "C"

string_names = ["E", "B", "G", "D", "A"]
all_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

### Functions ###
def get_notes_on_string(open_note):
    """Return the 12 notes on a string starting from its open note."""
    offset = all_notes.index(open_note)
    return [all_notes[(i + offset) % 12] for i in range(12)]

def is_note_in_scale(scale, note):
    """Check if a note is in the given major scale."""
    return note in major_scales[scale]

### Lists and dicts ###
notes_per_string = {name: get_notes_on_string(name) for name in string_names}
notes_per_strings_in_scale = {name: [] for name in string_names}
positions_on_strings_in_scale = {name: [] for name in string_names}

major_scales = {
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


### Loops ###
for string_name, string_notes in notes_per_string.items():
    for fret, note in enumerate(string_notes):
        if is_note_in_scale(selected_scale, note):
            notes_per_strings_in_scale[string_name].append(note)
            positions_on_strings_in_scale[string_name].append(fret)

for string_name in string_names:
    print(f"{string_name}: ", end="")
    for fret, note in enumerate(notes_per_string[string_name]):
        if note in notes_per_strings_in_scale[string_name]:
            print(f"{note}", end="-")
        else:
            print("x", end="-")
    print()