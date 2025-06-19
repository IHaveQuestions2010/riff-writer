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

def noteInScale(scale, isMajor, note):
    match isMajor:
        case 1:
            if note in majorScalesDict[scale]:
                return True
            else:
                return False
        case 0:
            if note in minorScalesDict[scale]:
                return True
            else:
                return False
        case _:
            raise Exception("something went wrong")

eString, eNotesPosition = notesOnAString("E")
bString, bNotesPosition = notesOnAString("B")
gString, gNotesPosition = notesOnAString("G")
dString, dNotesPosition = notesOnAString("D")
aString, aNotesPosition = notesOnAString("A")

note1 = []
position = []
noteInScalePlacment = [note1, position]

for note in eString:
    if noteInScale("C", 1, note) == 1:
        note1.append(note)
        position.append(eNotesPosition[eString.index(note)])
print(noteInScalePlacment)