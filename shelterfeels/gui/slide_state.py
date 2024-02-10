from enum import Enum

class SlideState(Enum):
    ZERO = 0 # possibly useful für starting animations or something
    START = 1
    RECORDING = 2
    RECORDING_OVER = 3
    WORD = 4
    END = 5
