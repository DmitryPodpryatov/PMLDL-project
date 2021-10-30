import matplotlib.pyplot as plt


def hist(data):
    labels, freq = zip(*data.items())

    plt.bar(labels, freq)
    plt.show()
