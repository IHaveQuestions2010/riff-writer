selected_scale = "C"

string_names = ["E", "B", "G", "D", "A"]
all_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

major_scales = {
    "C": ["C", "D", "E", "F", "G", "A", "B"], # All natural

    "G": ["G", "A", "B", "C", "D", "E", "F#"], # One sharp
    "D": ["D", "E", "F#", "G", "A", "B", "C#"], # Two sharps
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"], # Three sharps
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"], # Four sharps
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"], # Five sharps
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"], # Six sharps
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"], # Seven sharps

    "F": ["F", "G", "A", "A#", "C", "D", "E", "F"], # One flat   
    "Bb": ["A#", "C", "D", "D#", "F", "G", "A"], # Two flats
    "Eb": ["D#", "F", "G", "G#", "A#", "C", "D"], # Three flats
    "Ab": ["G#", "A#", "C", "C#", "D#", "F", "G"], # Four flats
    "Db": ["C#", "D#", "F", "F#", "G#", "A#", "C"], # Five flats
    "Gb": ["F#", "G#", "A#", "B", "C#", "D#", "F"], # Six flats
    "Cb": ["B", "C#", "D#", "Fb", "F#", "G#", "A#"] # Seven flats
}

display_scale_names = {
    "D#": "Eb",
    "G#": "Ab",
    "A#": "Bb",
    "C#": "Db",
    "F#": "Gb",
}