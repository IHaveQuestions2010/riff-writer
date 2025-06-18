baseTab = """e|---------------------------------------------------------------|
B|---------------------------------------------------------------|
G|---------------------------------------------------------------|
D|---------------------------------------------------------------|
A|---------------------------------------------------------------|
E|---------------------------------------------------------------|"""

majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]
allNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

currentNote = 0


def getScale(scale):
    notesOrder = []
    offset = allNotes.index(scale.capitalize())    
    for notes in range(len(allNotes)):
        notesOrder.append(allNotes[(notes+offset)%len(allNotes)])
    currentNote = 0
    notes = []
    for i in range(len(majorScale)):
        notes.append((notesOrder[currentNote]))
        currentNote = currentNote + majorScale[i]
    return notes
print(getScale("C#"))