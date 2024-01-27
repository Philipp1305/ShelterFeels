from tkinter import Tk, Label, Button

from typing import List
from random import choice


i = 1


def center_window(window: Tk) -> None:
    '''
    centers a window on any screen (respects titlebar)
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    '''

    window.update_idletasks()

    width = window.winfo_width()
    height = window.winfo_height()

    x = int(window.winfo_screenwidth()/2 - width/2)
    y = int(window.winfo_screenheight()/2 - height/2)

    window.geometry(f'{width}x{height}+{x}+{y}')


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

    global i # TODO: find solution that doesn't use global variables (probably just wrap in global object and write iterator)
    label.config(text=label_text_list[i], bg=color)

    i += 1
    if i >= len(label_text_list):
        i = 0


def build_window(keywords: List[str] = [
    'Hello, ma baby!',
    'Hello, ma honey!',
    'Hello, ma ragtime gaaaaaal!',
    'Send me a kiss by wire',
    'Baby, my heart\'s on fire!',
    ]
):
    '''serves as main for now'''

    width_height = 400

    tk = Tk()
    tk.configure(bg='red')
    tk.resizable(False, False)
    # tk.overrideredirect(True)

    tk.geometry(f'{width_height}x{width_height}')
    center_window(tk)

    label = insert_label(keywords[0], tk)
    label.config(bg='red')

    button = Button(tk, text='NEXT', command=lambda: next_button(keywords, label, tk))
    button.pack()

    tk.mainloop()


if __name__ == "__main__":
    build_window()
