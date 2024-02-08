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


def insert_label(label_text: str, window: Tk, relx: float, rely: float, type: str = "") -> Label:
    '''
    gives you a singular semi centered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :return: tkinter Label object we just inserted
    '''
    if type == "subtext":
        font_size = style.default_subtext_size
    else:
        font_size = style.default_text_size
    label = Label(window, text=label_text, 
                  font=(style.default_text_font, font_size),
                  bg=style.default_background)
    label.place(relx = relx, 
                rely = rely,
                anchor = 'center')
    return label


def switch_label_text(label: Label, text: str, subtext_label: Label = None, subtext: str = ""):
    label.config(text=text)
    if subtext_label:
        if subtext:
            subtext_label.config(text = subtext)
        else:
            subtext_label.config(text="")
