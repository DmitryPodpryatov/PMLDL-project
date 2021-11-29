import numpy as np
import soundfile as sf

from models import Track


def read_wav(filename: str) -> Track:
    data, sample_rate = sf.read(filename)

    return Track(filename, data, sample_rate)


def write_wav(filename: str, data: np.ndarray, sample_rate: int) -> None:
    sf.write(filename, data=data, samplerate=sample_rate)
