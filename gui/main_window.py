from gui.models.func_counter import funky
from gui.models.words import words
from gui.style import style
from gui.base_window import center_window
from gui.fancy_window_animations import insert_label
from tkinter import Tk


def build_the_main_window():
    '''builds a root window. all other functions follow afterwards'''

    width_height = style.default_window_size

    root = Tk()
    root.configure(bg=style.default_background)
    root.resizable(False, False)

    root.overrideredirect(True)

    # root.attributes("-fullscreen", True)
    # root.bind("<Button-3>", lambda x: root.attributes("-fullscreen", False))
    # root.bind("<Button-2>", lambda x: root.attributes("-fullscreen", False))
    root.geometry(f'{width_height}x{width_height}')

    center_window(root)
    words.label = insert_label('ShelterFeels', root)

    root.bind("<Button-1>", lambda event: funky.next_func(root))
    root.config(cursor="none")

    root.after(10, funky.next_func(root))
    root.mainloop()


if __name__ == "__main__":
    build_the_main_window()
