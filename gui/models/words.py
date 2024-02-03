from dataclasses import dataclass, field


@dataclass
class Words:
    conter: int = 0
    words: field(default_factory=list) = []

    def next_word(self) -> str:
        word = self.words[self.conter]
        self.conter += 1
        if self.counter >= len(self.words):
            self.counter = 0
        return word

words = Words()