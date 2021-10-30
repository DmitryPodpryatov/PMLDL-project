import music21
from music21.chord import Chord
from music21.note import Note
from music21.pitch import Pitch

from models import Track


def read(filename):
    notes = []

    midi = music21.converter.parse(filename)

    instruments = music21.instrument.partitionByInstrument(midi)

    for part in instruments.parts:
        music_units = part.recurse()

        for unit in music_units:
            if isinstance(unit, Note):
                notes.append(str(unit.pitch))

            if isinstance(unit, Chord):
                notes.append('.'.join(str(Pitch(n)) for n in unit.normalOrder))

    return Track(notes)
