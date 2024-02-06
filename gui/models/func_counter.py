from gui.keyword_handler import extract_words
from gui.models.words import words

from dataclasses import dataclass
from typing import Literal, Callable
from tkinter import Tk

from threading import Thread
# from gui.secondary_input import switcher
from time import sleep

# from led_testing_for_photo import full_circle
# full_circle()

def switcher():
    while True:
        sleep(5)
        print('hello')
        funky.next_func()
        print('world')


def show_words_and_wait(root):
    t1=Thread(target=switcher) 
    t1.start() 
    words.show_next_keyword(root)


@dataclass
class Funky:
    next_screen = False
    func_count: int = 0
    func_list = [
        'RECORD',
        'WORD',
        'WORD',
        'WORD',
        'EXIT'
    ]
    root: Tk = None

    def next_func(self) -> None:
        print('next func called')
        print(f'func count: {self.func_count}')
        command = self.func_list[self.func_count]
        selected = self.select_func(command)
        self.next_screen = selected(self.root)
        self.func_count += 1
        if self.func_count >= len(self.func_list):
            self.func_count = 0
        # if self.next_screen:
        #     self.next_func(root)


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
                selected_func = show_words_and_wait
            case 'LED_ADJUST':
                pass
            case 'EXIT':
                selected_func = self.quit_root
            case _:
                pass

        return selected_func
    
    def quit_root(self, root):
        root.destroy()



funky = Funky()
