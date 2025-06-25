from variables import all_notes, major_scales

def get_notes_on_string(open_note):
    offset = all_notes.index(open_note)
    return [all_notes[(i + offset) % 12] for i in range(12)]

def is_note_in_scale(scale, note):
    return note in major_scales[scale]

def generate_fretboard_for_scale(scale, string_names):
    notes_per_string = {name: get_notes_on_string(name) for name in string_names}
    notes_in_scale = {name: [] for name in string_names}
    frets_in_scale = {name: [] for name in string_names}

    for string_name, string_notes in notes_per_string.items():
        for fret, note in enumerate(string_notes):
            if is_note_in_scale(scale, note):
                notes_in_scale[string_name].append(note)
                frets_in_scale[string_name].append(fret)
    return notes_per_string, notes_in_scale, frets_in_scale
