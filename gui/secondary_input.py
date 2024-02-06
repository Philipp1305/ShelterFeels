'''
let's think about how the actual process needs to look like
1. we create a window
2. the window will have 2 inputs:
    - a click event
    - a secondary event
therefore, we will need to two threads: one watching the button event, the second watching our secondary input
'''

from time import sleep

def switcher():
    while True:
        sleep(1)
        print('hello')
        print('world')