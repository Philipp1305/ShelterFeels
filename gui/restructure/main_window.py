from style import style
from window_utility import center_window, insert_label, switch_label_text
from slide_state import SlideState
from stoppable_thread import StoppableThread

# from gui.restructure.style import style
# from gui.restructure.window_utility import center_window, insert_label

from typing import Set
from tkinter import Tk, Label
from time import sleep


class MainWindow(Tk):
    slide_state: SlideState
    label: Label
    word_set: Set[str]

    second_thread: StoppableThread

    def __init__(self):
        Tk.__init__(self) # tkinter uses old style classes

        self.geometry(f'{style.default_window_size}x{style.default_window_size}')
        self.configure(bg=style.default_background)

        self.resizable(False, False)
        if not style.has_titlebar:
            self.overrideredirect(True)

        self.config(cursor="none")

        center_window(self)

        self.label = insert_label('ShelterFeels', self)
        self.slide_state = SlideState.START
        self.word_set = set()
        self.second_thread = None

        self.bind("<Button-1>", lambda event: self.next_slide())
        self.after(3000, self.next_slide)


    def next_slide(self):
        print(self.slide_state.value)
        if self.second_thread:
            if not self.second_thread.stopped():
                print('stopping thread')
                self.second_thread.stop()

        match self.slide_state:
            case SlideState.START:
                switch_label_text(self.label, 'Start recording?')
                self.slide_state = SlideState.RECORDING
            case SlideState.RECORDING:
                
                self.word_set.update(['hello', 'my', 'darling', 'red', 'blue', 'yellow', 'green'])
                self.slide_state = SlideState.WORD
            case SlideState.WORD:
                if self.word_set:
                    word = self.word_set.pop()
                    print(word)
                    self.second_thread = StoppableThread(target=self.thread_test, daemon=True)
                    self.second_thread.start()
                    switch_label_text(self.label, word)


    def thread_test(self):
        print('thread')
        sleep(10)
        self.next_slide()


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
