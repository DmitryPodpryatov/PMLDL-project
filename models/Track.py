from dataclasses import dataclass, field

import numpy as np


@dataclass(repr=False)
class Track:
    filename: str
    data: np.ndarray
    sample_rate: int
    length: float = field(init=False)

    def __post_init__(self):
        self.length = len(self.data) / self.sample_rate

    def __repr__(self):
        return f'{{ filename={self.filename},\n' \
               f' sample_rate={self.sample_rate},\n' \
               f' length={self.length:.3f}s }}'
