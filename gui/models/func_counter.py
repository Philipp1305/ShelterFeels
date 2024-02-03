from gui.keyword_handler import extract_words
from gui.models.words import words

from dataclasses import dataclass
from typing import Literal, Callable
from tkinter import Tk

@dataclass
class Funky:
    func_count: int = 0
    func_list = [
        'RECORD',
        'WORD',
        'WORD',
    ]

    def next_func(self, root: Tk) -> None:
        print('next func called')
        command = self.func_list[self.func_count]
        selected = self.select_func(command)
        selected(root)
        self.func_count += 1
        if self.func_count >= len(self.func_list):
            self.func_count = 0

    def select_func(self, selector: Literal[
        'START',
        'RECORD_START',
        'RECORD',
        'RECORD_PROCESS',
        'WORD',
        'LED_ADJUST'
        ]) -> (Callable | None):

        selected_func = None
        match selector:
            case 'START':
                pass
            case 'RECORD_START':
                pass
            case 'RECORD':
                selected_func = extract_words
            case 'RECORD_PROCESS':
                pass
            case 'WORD':
                selected_func = words.show_next_keyword
            case 'LED_ADJUST':
                pass

        return selected_func

funky = Funky()
