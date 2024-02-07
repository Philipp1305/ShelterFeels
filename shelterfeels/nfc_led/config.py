from enum import Enum
from pathlib import Path

number_of_leds = 84
number_of_led_in_circle = 12
json_path = Path(__file__).parent.parent / "colors.json"
todays_colors_json_path = Path(__file__).parent.parent / "todays_colors.json"

class Day(Enum): # day to led number 
    friday= 0
    thursday= 1
    saturday= 2
    sunday= 3
    monday= 4
    wendsday= 5
    tuesday= 6
    
daynum_to_day = {
    "0": Day.monday,
    "1": Day.tuesday,
    "2": Day.wendsday,
    "3": Day.thursday,
    "4": Day.friday,
    "5": Day.saturday,
    "6": Day.sunday
}
    
brightness_scale = 0.1 # from 0 to 1
    
class Emotion(Enum):
    joyful = (255, 246, 8)
    powerful = (50, 200, 15)
    peaceful = (12, 102, 203)
    sad = (150, 19, 220)
    mad = (255 , 10, 0)
    scared = (200, 67, 0)
    '''joyful = (128, 123, 4)
    powerful = (25, 74, 7)
    peaceful = (6, 51, 101)
    sad = (75, 9, 99)
    mad = (101, 15 , 15)
    scared = (178, 113, 15) '''   

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