
from shelterfeels.nfc_led.nfc import read_emotion_from_nfc
from shelterfeels.nfc_led.neo_pixel import fill_circle, turn_off, upload_day_state, load_state
from shelterfeels.nfc_led.config import daynum_to_day
from datetime import datetime

if __name__ == "__main__":
    for weekday in range(0, 7):
        day = daynum_to_day[weekday]
        colors = []
        try:
            while True:
                emotion = read_emotion_from_nfc()
                print(emotion)
                colors.append(emotion.value)
                print (colors)
                fill_circle(day, colors)
                upload_day_state(weekday, colors)
        except KeyboardInterrupt:
            continue