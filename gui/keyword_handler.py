from voice_recognition_app.inference_remote import extract_key_words_online
from gui.models.func_counter import counter
from gui.models.words import words

from tkinter import Tk, Label
from typing import List


def insert_label(label_text: str, window: Tk) -> Label:
    '''
    gives you a singular semi centered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :return: tkinter Label object we just inserted
    '''

    label = Label(window, text=label_text, font=('Comic Sans MS', 18))

    label_height = int(window.winfo_height()/2 - 30)
    label.pack(pady=label_height) # TODO: absolute positions

    return label


def show_next_keyword(window: Tk) -> None:
    '''
    for adding the keywords extracted by voice_recognition inference
    :param window: tkinter Tk root object
    '''

    label = insert_label(words.next_word(), window)
    label.config(bg='red')

    return


def extract_words():
    keywords = extract_key_words_online()
    if not keywords:
        print('ERROR. No keywords extracted')
        return
    words.words = keywords
