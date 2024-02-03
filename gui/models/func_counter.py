from gui.keyword_handler import extract_words
from gui.models.words import words

from dataclasses import dataclass
from typing import Literal, Callable
from tkinter import Tk
from nfc_led_connection import read_nfc_and_change_led

@dataclass
class Funky:
    next_screen = False
    func_count: int = 0
    func_list = [
        'RECORD',
        'WORD',
        'WORD',
        'WORD',
    ]

    def next_func(self, root: Tk) -> None:
        print('next func called')
        print(f'func count: {self.func_count}')
        command = self.func_list[self.func_count]
        selected = self.select_func(command)
        self.next_screen = selected(root)
        self.func_count += 1
        if self.func_count >= len(self.func_list):
            self.func_count = 0
        if self.next_screen:
            self.next_func(root)


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
                # NOTE: always call word an additional time to destroy the label
                selected_func = words.show_next_keyword
            case 'LED_ADJUST':
                pass
            case _:
                pass
                

        return selected_func

funky = Funky()
