'''
because the canonical way to manipulate a root in tkinter is .after()
we should implement the root as the main function
'''
from gui.base_window import center_window
from gui.keyword_handler import add_keywords
from tkinter import Tk


def main():
    '''builds a root window. all other functions follow afterwards'''

    width_height = 400

    root = Tk()
    root.configure(bg='red')
    root.resizable(False, False)
    root.overrideredirect(True)

    root.geometry(f'{width_height}x{width_height}')
    center_window(root)


    # this will allow us to build a root and then do some action. ANY action
    root.after(1000, lambda: add_keywords(root))

    root.mainloop()


if __name__ == "__main__":
    main()
