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
    '''joyful = (255, 246, 8)
    powerful = (50, 148, 15)
    peaceful = (12, 102, 203)
    sad = (150, 19, 198)
    mad = (202 ,31 ,31)
    scared = (243, 147, 50)'''
    joyful = (136, 123, 8)
    powerful = (50, 74, 15)
    peaceful = (12, 51, 101)
    sad = (75, 19, 100)
    mad = (101 ,31 ,31)
    scared = (240, 145, 51)    

nfc_to_emotion = {
    '1068074383812618542': Emotion.joyful,
    '10680744223517110438': Emotion.joyful,
    '10680741024411418642': Emotion.joyful,
    '1068074695311318642': Emotion.powerful,
    '10680741642212718542': Emotion.powerful,
    '10680743323711218642': Emotion.powerful,
    '10680742317017110438': Emotion.peaceful,
    '106807421212517310438': Emotion.peaceful, 
    '10680743613317210438': Emotion.peaceful,
    '106807420523812518542': Emotion.sad,
    '10680741664317110438': Emotion.sad,
    '106807419825412518542': Emotion.sad,
    '106807423923216710438': Emotion.mad,
    '10680741966311418642': Emotion.mad,
    '106807412016617110438': Emotion.mad,
    '10680741091911318642': Emotion.scared,
    '10680746124417110438': Emotion.scared,
    '106807422814517110438': Emotion.scared,
}

# ALSO NEED ENUM EMOTION TO COLOR