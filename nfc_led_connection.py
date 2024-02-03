from datetime import datetime
from nfc import read_emotion_from_nfc
from neo_pixel import fill_circle, turn_off

colors = []
def read_nfc_and_change_led(*args):
    """
    Read nfc and adds new color to the circle
    """
    weekday = datetime.today().weekday()
    emotion = read_emotion_from_nfc()
    print(emotion)
    colors.append(emotion.value)
    print (colors)
    # fill_circle(weekday, colors)
    pass # funky.next() in the end.

def finish_day():
    """makes the day empty"""
    global colors
    colors = []
    # todo write in json 
    
if __name__ == "__main__":
    # for i in range(5):
    #     read_nfc_and_change_led()
    # finish_day()
    # print(colors)
    for i in range(5):
        read_nfc_and_change_led()
    turn_off()