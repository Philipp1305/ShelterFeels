'''
because the canonical way to manipulate a window in tkinter is .after()
we should implement the window as the main function
'''
from gui.base_window import center_window
from gui.keyword_handler import add_keywords
from tkinter import Tk

def on_click(event):
    print("you clicked")


def main():
    '''builds a base window. all other functions follow afterwards'''

    width_height = 400

    root = Tk()
    root.configure(bg='red')
    root.resizable(False, False)
    root.overrideredirect(True)

    root.geometry(f'{width_height}x{width_height}')
    center_window(root)

    # add_keywords(root)

    # this will allow us to build a window and then do some action. ANY action
    root.after(1000, add_keywords(root))

    root.mainloop()


if __name__ == "__main__":
    main()
