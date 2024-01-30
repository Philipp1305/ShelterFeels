from gui.counter import counter

from tkinter import Tk, Label
from typing import List
from random import choice


def insert_label(label_text: str, window: Tk) -> Label:
    '''
    gives you a singular semi centered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :return: tkinter Label object we just inserted
    '''

    label = Label(window, text=label_text, font=('Comic Sans MS', 18))

    label_height = int(window.winfo_height()/2 - 30)
    label.pack(pady=label_height-100) # TODO: absolute positions

    return label


def next_button(label_text_list: List[str], label: Label, window: Tk) -> None:
    '''
    sets label text by iterating over list with a global variable i
    :label_text_list: list of text we want to iterate over
    :label: tkinter Label object
    :canvas: tkinter Canvas object to change color
    '''
    color = choice(["red" , "green" , "blue"])  # TODO: obviously, we need a static color picking system

    window.configure(bg=color)
    if color == 'blue':
        label.config(fg='white')
    else:
        label.config(fg='black')

    label.config(text=label_text_list[counter.button_count], bg=color)

    counter.button_count += 1
    if counter.button_count >= len(label_text_list):
        counter.button_count = 0


def add_keywords(window: Tk,
                 keywords: List[str] = [
    'Hello, ma baby!',
    'Hello, ma honey!',
    'Hello, ma ragtime gaaaaaal!',
    'Send me a kiss by wire',
    'Baby, my heart\'s on fire!',
    ]
    ) -> None:
    '''for adding the keywords extracted by voice_recognition inference'''

    label = insert_label(keywords[0], window)
    label.config(bg='red')


    window.bind("<Button-1>", lambda event: next_button(keywords, label, window))

    return
