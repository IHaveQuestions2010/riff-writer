baseTab = """e|---------------------------------------------------------------|
B|---------------------------------------------------------------|
G|---------------------------------------------------------------|
D|---------------------------------------------------------------|
A|---------------------------------------------------------------|
E|---------------------------------------------------------------|"""

allNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

majorScalesDict = {
    "C": ["C", "D", "E", "F", "G", "A", "B"], # All natural

    "G": ["G", "A", "B", "C", "D", "E", "F#"], # One sharp
    "D": ["D", "E", "F#", "G", "A", "B", "C#"], # Two sharps
    "A":["A", "B", "C#", "D", "E", "F#", "G#"], # Three sharps
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"], # Four sharps
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"], # Five sharps
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"], # Six sharps
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"], # Seven sharps

    "F": ["F", "G", "A", "Bb", "C", "D", "E", "F"], # One flat   
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"], # Two flats
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"], # Three flats
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"], # Four flats
    "Db":  ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], # Five flats
    "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"], # Six flats
    "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"] # Seven flats
}

minorScalesDict = {
    "Am": majorScalesDict["C"], # All naturals

    "Em": majorScalesDict["G"], # One sharp
    "Bm": majorScalesDict["D"], # Two sharps
    "F#m": majorScalesDict["A"], # Three sharps
    "C#m": majorScalesDict["E"], # Four sharps
    "G#m": majorScalesDict["B"], # Five sharps
    "D#m": majorScalesDict["F#"], # Six sharps
    "A#m": majorScalesDict["C#"], # Seven sharps

    "Dm": majorScalesDict["F"], # One flat
    "Gm": majorScalesDict["Bb"], # Two flats
    "Cm": majorScalesDict["Eb"], # Three flats
    "Fm": majorScalesDict["Ab"], # Four flats
    "Bbm": majorScalesDict["Db"], # Five flats
    "Ebm": majorScalesDict["Gb"], # Six flats
    "Abm": majorScalesDict["Cb"] # Seven flats
}

def notesOnAString(string):
    offset = allNotes.index(string)
    notes = []
    stringPosition = []
    for note in range(12):
        notes.append(allNotes[(note+offset)%12])
    for note in notes:
        stringPosition.append(notes.index(note))
    return notes, stringPosition