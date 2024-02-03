from gui.fancy_window_animations import insert_label, switch_label_text
from dataclasses import dataclass
from tkinter import Tk, Label


@dataclass
class Words:

    label: Label = None
    counter: int = 0
    words = []


    def next_word(self) -> str:
        print(self.counter)
        word = self.words[self.counter]
        self.counter += 1
        if self.counter >= len(self.words):
            self.counter = 0
        return word


    def show_next_keyword(self, window: Tk) -> None:
        '''
        for adding the keywords extracted by voice_recognition inference
        :param window: tkinter Tk root object
        '''
        if not self.label:
            self.label = insert_label(self.next_word(), window)
            return

        if len(self.words) <= self.counter:
            self.label.destroy()
            return

        switch_label_text(self.label, self.next_word())
        return


words = Words()
