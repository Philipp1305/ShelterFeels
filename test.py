from shelterfeels.nfc_led.config import Day, Emotion
from shelterfeels.nfc_led.neo_pixel import upload_day_state, fill_circle, load_state, turn_off
from time import sleep
if __name__ == "__main__":
    # upload_current_state()
    fill_circle(Day.monday, [(0, 255, 0), (255, 0, 0), (0, 0, 255), (100, 50,0)])
    # upload_current_state()
    # sleep(3)
    turn_off()
    # sleep(3)
    # load_state()
    # t = 5
    # fill_circle(0, [(0, 255, 0), ])
    # sleep(t)
    # fill_circle(1, [(0, 255, 0), (255, 0, 0)])
    # sleep(t)
    # fill_circle(2, [(0, 255, 0), (255, 0, 0), (0, 0, 255)])
    # sleep(t)
    # fill_circle(3, [(0, 255, 0), (255, 0, 0), (0, 0, 255), (100, 50,0)])
    # sleep(t)
    # fill_circle(4, [(0, 255, 255)])
    # sleep(t)
    # fill_circle(5, [(0, 255, 255), (255, 255, 0),])
    # sleep(t)
    # fill_circle(6, [(0, 255, 255), (255, 255, 0), (0, 255, 255),])
    # sleep(t)
    
    upload_day_state(0, [Emotion.mad.value,
                    Emotion.sad.value,
                    Emotion.scared.value])
    
    upload_day_state(1, [Emotion.powerful.value,
                    Emotion.sad.value])
    
    upload_day_state(2, [Emotion.mad.value,
                    Emotion.scared.value])
    
    upload_day_state(3, [Emotion.joyful.value,
                    Emotion.peaceful.value,
                    Emotion.powerful.value,
                    Emotion.mad.value])
    
    upload_day_state(4, [Emotion.joyful.value,
                    Emotion.mad.value,
                    Emotion.peaceful.value])
    
    upload_day_state(5, [Emotion.scared.value,
                    Emotion.sad.value,
                    Emotion.joyful.value])
    
    upload_day_state(6, [Emotion.mad.value,
                    Emotion.sad.value])
    
    