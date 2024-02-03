from voice_recognition_app.inference_remote import extract_key_words_online
from gui.keyword_handler import extract_words, show_next_keyword

from dataclasses import dataclass
from typing import Literal, Callable
from tkinter import Tk

@dataclass
class Funky:
    func_count: int = 0
    func_list = [
        'START',
        'RECORD_START',
        'RECORD',
        'RECORD_PROCESS',
        'WORD',
        'LED_ADJUST'
    ]

    def next_func(self, root: Tk) -> None:
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
                selected_func = show_next_keyword
            case 'LED_ADJUST':
                pass

        return selected_func

funky = Funky()
