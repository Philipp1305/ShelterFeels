from gui.models.func_counter import funky
from gui.config_gui import gui_settings
from gui.base_window import center_window
from tkinter import Tk


def build_the_main_window():
    '''builds a root window. all other functions follow afterwards'''

    width_height = 400

    root = Tk()
    root.configure(bg=gui_settings.default_background)
    root.resizable(False, False)
    root.overrideredirect(True)

    root.geometry(f'{width_height}x{width_height}')
    center_window(root)

    root.bind("<Button-1>", lambda event: funky.next_func(root))

    root.mainloop()


if __name__ == "__main__":
    build_the_main_window()
