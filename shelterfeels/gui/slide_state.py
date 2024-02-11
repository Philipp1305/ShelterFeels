from enum import Enum, auto

class SlideState(Enum):
    ZERO = auto() # possibly useful für starting animations or something
    START = auto()
    RECORDING = auto()
    PLEASEWAIT = auto()
    WORDEXPLAINONE = auto()
    WORDEXPLAINTWO = auto()
    WORD = auto()
    END = auto()
