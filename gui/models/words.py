from gui.fancy_window_animations import insert_label, switch_label_text
from dataclasses import dataclass
from tkinter import Tk, Label
# from nfc_led_connection import read_nfc_and_change_led

@dataclass
class Words:

    label: Label = None
    counter: int = 0
    words = []


    def next_word(self) -> str:
        print(self.counter)
        word = self.words[self.counter]
        self.counter += 1
        return word


    def show_next_keyword(self, window: Tk) -> None:
        '''
        for adding the keywords extracted by voice_recognition inference
        :param window: tkinter Tk root object
        '''

        if not self.label:
            print('insert label')
            self.label = insert_label(self.next_word(), window)
            print("HERE", self.label)
            window.update()
            # read_nfc_and_change_led()
            return True

        print(f'count: {self.counter}, words: {len(self.words)}')
        if self.counter >= len(self.words):
            self.counter = 0
            print('DESTROY')
            self.label.destroy() # maybe move this destroy to start next function in pipeline
            self.label = None
            return True
        
        switch_label_text(self.label, self.next_word())
        print("HERE", self.label)
        window.update()
        # read_nfc_and_change_led()

        return True
    
# def show_word(words, window: Tk):
#     for word in words:
        

words = Words()
