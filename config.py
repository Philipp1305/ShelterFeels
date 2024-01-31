from enum import Enum
number_of_leds = 84
number_of_led_in_circle = 12

class Day(Enum):
    monday= 0
    tuesday= 1
    wendsday= 2
    thursdat= 3
    friday= 4
    sunday= 5
    saturday= 6
    
class Emotion(Enum):
    joyful = (255,255,0)
    powerful = (0,153,51)
    peaceful = (51,51,255)
    sad = (153,51,153)
    mad = (255,0,0)
    scared = (255,153,0)
    
nfc_to_emotion = {
    '1068074383812618542': Emotion.joyful,
    '1068074695311318642': Emotion.powerful,
    '10680742317017110438': Emotion.peaceful,
    '106807420523812518542': Emotion.sad,
    '106807423923216710438': Emotion.mad,
    '10680741091911318642': Emotion.scared
}

# ALSO NEED ENUM EMOTION TO COLOR