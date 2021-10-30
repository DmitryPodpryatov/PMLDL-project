from music.midi import read
from music import stats
from visual import hist


def read_midi():
    midi_file = 'midi/track.mid'

    return read(midi_file)


def print_stats(track):
    dist = stats.distribution(track.notes)

    print(track)
    print(len(stats.unique(track.notes)))
    print(dist)

    hist(dict(dist.most_common(10)))


def main():
    track = read_midi()
    print_stats(track)


if __name__ == '__main__':
    main()
