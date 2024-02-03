from tkinter import Tk


def center_window(window: Tk) -> None:
    '''
    centers a window on any screen (respects titlebar)
    :param window: tkinter Tk object. should be a toplevel window, not a widget
    '''

    window.update_idletasks()

    width = window.winfo_width()
    
    height = window.winfo_height()
    # titlebar_height = window.winfo_rooty() - window.winfo_y()
    # frm_width = window.winfo_rootx() - window.winfo_x()
    # actual_height = height + titlebar_height + frm_width

    x = int(round(window.winfo_screenwidth()/2 - width/2))
    y = int(round(window.winfo_screenheight()/2 - height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')
