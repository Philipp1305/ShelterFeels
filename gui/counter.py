from dataclasses import dataclass

@dataclass
class Counter:
    button_count: int = 1

counter = Counter()
