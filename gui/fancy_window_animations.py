from gui.config_gui import gui_settings
from tkinter import Tk, Label


def insert_label(label_text: str, window: Tk) -> Label:
    '''
    gives you a singular semi centered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :return: tkinter Label object we just inserted
    '''

    label = Label(window, text=label_text, font=(gui_settings.default_text_font, 18))
    label.config(bg=gui_settings.default_background)

    label_height = int(window.winfo_height()/2 - 30)
    label.pack(pady=label_height) # TODO: absolute positions

    return label


def switch_label_text(label: Label, text: str):
    label.config(text=text)
