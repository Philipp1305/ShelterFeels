from tkinter import Tk, Label


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


def insert_label(new_label: str, window: Tk, old_label: Label = None) -> Label:
    '''
    gives you a semi entered text in the given window
    :param new_label: any string, preferably not too long
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    :param old_label: a label created with insert_label
    :return: tkinter Label object we just inserted
    '''

    if old_label:
        old_label.destroy()

    label = Label(window, text=new_label, font=('Comic Sans MS', 18))

    label_height = int(window.winfo_height()/2 - 30)
    label.pack(pady=label_height)

    return label


def build_window():
    '''serves as main for now'''

    width_height = 480

    tk = Tk()
    tk.resizable(False, False)
    tk.overrideredirect(True)

    tk.geometry(f'{width_height}x{width_height}')
    center_window(tk)

    label = insert_label('Hello', tk)
    label = insert_label('World', tk, label)

    tk.mainloop()


if __name__ == "__main__":
    build_window()
