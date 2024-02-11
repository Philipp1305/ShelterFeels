from shelterfeels.gui.window_utility import center_window, insert_label, switch_label_text
from shelterfeels.gui.slide_state import SlideState
from shelterfeels.gui.style import style
from shelterfeels.nfc_led.nfc_led_connection import read_nfc_and_change_led

from shelterfeels.voice_recognition_app.inference_remote import send_post
from shelterfeels.voice_recognition_app.recognition.audio_utils import record_until_interrupt
from shelterfeels.voice_recognition_app.config import records_folder

from tkinter import Tk, ttk
from time import sleep
from multiprocessing import Process, Manager
from textwrap import dedent
from datetime import datetime


class MainWindow(Tk):
    '''
    label: Label
    word_list: List[str]
    nfc_process: Process
    slide_state: SlideState
    '''

    def __init__(self):
        Tk.__init__(self) # tkinter uses old style classes

        '''window configurations'''
        self.geometry(f'{style.default_window_size}x{style.default_window_size}')
        self.configure(bg=style.default_background)

        self.config(cursor="none")
        self.resizable(False, False)
        if not style.has_titlebar:
            self.overrideredirect(True)

        center_window(self)
        '''attributes'''
        self.label = insert_label('ShelterFeels', self, rely=0.4, relx=0.5) # any intro animation would go here
        self.subtext_label = insert_label('click to proceed or wait', self, relx=0.5, rely = 0.6, type="subtext")
        self.slide_state = SlideState.START

        manager = Manager()
        self.word_list = manager.list()
        self.nfc_process = None

        self.progress = None


        '''interaction'''
        self.bind("<Button-1>", lambda event: self.next_slide())
        self.after(20000, self.first_slide)



    def first_slide(self):
        if self.slide_state == SlideState.START:
            self.next_slide()


    def next_slide(self):
        '''
        based on the current slide state, doe something and moves the state forward if needed
        also checks for loose child processes and kills them
        '''
        self.update_idletasks()

        if self.nfc_process is not None:
            if self.nfc_process.is_alive():
                self.nfc_process.terminate()
                print('thread terminated')
                sleep(0.1)

        match self.slide_state:
            case SlideState.START:
                switch_label_text(self.label, 'Start recording?', self.subtext_label, "click to proceed")
                self.slide_state = SlideState.RECORDING

            case SlideState.RECORDING:
                switch_label_text(self.label, '', self.subtext_label, "please speak to the device \nfor at least a minute")

                self.nfc_process = Process(target=record_until_interrupt, daemon=True) # voice recording here
                self.nfc_process.start()

                s = ttk.Style()
                s.theme_use('clam')
                s.configure("bar.Horizontal.TProgressbar", foreground='red', background='red')
                self.progress = progress = ttk.Progressbar(self, style="bar.Horizontal.TProgressbar", length=300, mode='determinate')
                progress.place(rely=0.4, relx=0.2)
                start = datetime.now()
                progress.start(60)

                self.unbind("<Button-1>")
                self.update()
                while progress['value'] < 99:
                    # print(progress['value'])
                    sleep(0.01)
                    self.update()
                s.configure("bar.Horizontal.TProgressbar", background='blue')
                progress.stop()
                end = datetime.now()
                print('real time: ', (end - start))
                progress['value'] = 100
                self.update()
                print(progress['value'])
                self.bind("<Button-1>", lambda event: self.next_slide())

                self.slide_state = SlideState.PLEASEWAIT


            case SlideState.PLEASEWAIT:
                self.unbind("<Button-1>")
                if self.progress:
                    self.progress.destroy()

                filename = records_folder / 'recording.wav'
                self.nfc_process = Process(target=send_post, args=[filename, self.word_list], daemon=True) # voice recording here
                self.nfc_process.start()

                switch_label_text(self.label, 'processing...', self.subtext_label, "this should only take a few seconds")


                self.slide_state = SlideState.WORDEXPLAIN
                self.after_idle(self.check_process)



            case SlideState.WORDEXPLAIN:
                self.bind("<Button-1>", lambda event: self.next_slide())

                instruction = dedent('''
                                    next you will see some of the words
                                    you used to describe your day.
                                    think on how they make you feel,
                                    grab the corresponding tag
                                    and hold it underneath the screen'''
                                    )
                switch_label_text(self.label, 'complete', self.subtext_label, instruction)
                self.slide_state = SlideState.WORD


            case SlideState.WORD:
                word = self.word_list.pop()
                if not self.word_list:
                    self.slide_state = SlideState.END
                print(word)

                switch_label_text(self.label, word, self.subtext_label, "tag with an emotion token \nor touch to skip")
                self.nfc_process = Process(target=read_nfc_and_change_led, daemon=True) # nfc reading here
                self.nfc_process.start()
                self.after_idle(self.check_process)

            case SlideState.END:
                switch_label_text(self.label, 'DONE', self.subtext_label, "see you tomorrow!")
                self.after(2000, self.destroy)


    def check_process(self):
        if not self.nfc_process.is_alive():
            print('thread terminated')
            self.nfc_process.terminate()
            self.next_slide()
        else:
            self.after(200, self.check_process)


def thread_test():
    print('thready mcthread thread')
    sleep(3)
    return


def thread_test_recoding(string):
    print('recording process')
    string.value += 'file.name'
    sleep(1000)


def thread_test_keywords(string, list):
    # while True:

    print('threads again')
    print(string.value)
    if string.value == 'file.name':
        print('yes')
        list += ['hello', 'darkness', 'my', 'old', 'friend']
    sleep(10)


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
