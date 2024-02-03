from datetime import datetime
from nfc import read_emotion_from_nfc
from neo_pixel import fill_circle, turn_off
from config import Emotion
from time import sleep

def full_circle():
    fill_circle(0, [Emotion.mad.value,
                    Emotion.sad.value,
                    Emotion.scared.value])
    
    fill_circle(1, [Emotion.powerful.value,
                    Emotion.sad.value])
    
    fill_circle(2, [Emotion.mad.value,
                    Emotion.scared.value])
    
    fill_circle(3, [Emotion.joyful.value,
                    Emotion.peaceful.value,
                    Emotion.powerful.value,
                    Emotion.mad.value])
    
    fill_circle(4, [Emotion.joyful.value,
                    Emotion.mad.value,
                    Emotion.peaceful.value])
    
    fill_circle(5, [Emotion.scared.value,
                    Emotion.sad.value,
                    Emotion.joyful.value])
    
    fill_circle(6, [Emotion.mad.value,
                    Emotion.sad.value])
    
if __name__ == "__main__":
    full_circle()
    # sleep(30)
    # turn_off()