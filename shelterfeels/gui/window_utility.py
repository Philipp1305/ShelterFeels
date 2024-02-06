from shelterfeels.gui.style import style

from tkinter import Tk, Label


def center_window(window: Tk) -> None:
    '''
    centers a window on any screen (respects titlebar)
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    '''

    window.update_idletasks()

    width = window.winfo_width()
    
    height = window.winfo_height()

    x = int(round(window.winfo_screenwidth()/2 - width/2))
    y = int(round(window.winfo_screenheight()/2 - height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')


def insert_label(label_text: str, window: Tk) -> Label:
    '''
    gives you a singular semi centered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :return: tkinter Label object we just inserted
    '''

    label = Label(window, text=label_text, font=(style.default_text_font, style.default_text_size))
    label.config(bg=style.default_background)

    label_height = int(window.winfo_height()/2 - 30)
    label.pack(pady=label_height)

    return label


def switch_label_text(label: Label, text: str):
    label.config(text=text)

