from shelterfeels.nfc_led.nfc import read_emotion_from_nfc
from shelterfeels.nfc_led.neo_pixel import fill_circle, turn_off, upload_day_state, load_state_file
from shelterfeels.nfc_led.config import daynum_to_day
from datetime import datetime


def read_nfc_and_change_led(*args):
    """
    Read nfc and adds new color to the circle
    """
    weekday = str(datetime.today().weekday())
    day = daynum_to_day[weekday]
    colors = load_state_file()[weekday]
    emotion = read_emotion_from_nfc()
    print(emotion)
    colors.append(emotion.value)
    print (colors)
    fill_circle(day, colors)
    upload_day_state(weekday, colors)
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