from collections import Counter


def unique(notes):
    return list(set(notes))


def distribution(notes):
    counter = Counter(notes)

    return counter
