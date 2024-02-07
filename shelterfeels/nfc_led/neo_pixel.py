from shelterfeels.nfc_led.config import number_of_leds, number_of_led_in_circle, Day, brightness_scale, json_path, daynum_to_day

from time import sleep
from typing import Union
import json

import board
import neopixel


try:
    pixels = neopixel.NeoPixel(board.D18, number_of_leds) # 84 is number of LEDs
except Exception:
    print("bad led connection")
    pixels = None

def upload_day_state(daynum, color):
    print("Uploading state", daynum, color)
    colors = json.load(open(json_path, "r"))
    colors[daynum] = color
    print(colors)
    with open(json_path, "w") as f:
        json.dump(colors, f, indent=2)

def load_state():
    with open(json_path, "r") as f:
        colors = json.load(f)
        print("Loading state:", colors)
        for daynum, color in colors.items():
            fill_circle(daynum_to_day[daynum], color)
    return colors
           

def blink_color(color: tuple, time: int):
    if pixels is None:
        return
    pixels.fill([x * brightness_scale for x in color])
    pixels.show()                
    sleep(1)

    pixels.fill((0,0,0))
    pixels.show()
    sleep(1)
    
def one_pixel_fill(led_number: int, color: tuple, time: int):
    if pixels is None:
        return
    pixels[led_number] = [x * brightness_scale for x in color]
    pixels.show()                
    sleep(1)

    pixels[led_number] = 0,0,0
    pixels.show()
    sleep(1)
    
def turn_off():
    if pixels is None:
        return
    pixels.fill((0,0,0))
    pixels.show()
    
def fill_circle(circle_number: Union[int, Day], colors: list[tuple[int, int, int]], number_of_led_in_circle:int = number_of_led_in_circle ):
    """
    Highlights circle with given colors. 
    
    circle_number - nhumber of exact LED  or day that should be highligthed
    colors - array of RGB tuples that should be displayed. Size not more than number_of_led_in_circle
    number_of_led_in_circle - number of LED in each circle
    """
    if pixels is None:
        return
    if len(colors) == 0:
        colors = [(0,0,0)]
    if len(colors) > number_of_led_in_circle:
        print(f"Bad number of colors = {len(colors)}, more than number_of_led_in_circle={number_of_led_in_circle}")
        return
    if isinstance(circle_number, Day):
        circle_number = circle_number.value
    each_color_quantity = number_of_led_in_circle // len(colors)
    for num, color in enumerate(colors):
        left = circle_number*number_of_led_in_circle + num*each_color_quantity
        right = circle_number*number_of_led_in_circle + (num+1)*each_color_quantity
        print(color, "left", left, "right", right)
        if right > circle_number*number_of_led_in_circle + number_of_led_in_circle:
            right = circle_number*number_of_led_in_circle + number_of_led_in_circle
        for v in range(left, right): # set color
            pixels[v] = [x * brightness_scale for x in color]
    pixels.show()

if __name__ == "__main__":
    # LED control
    # blink_color((0, 255, 0), 1)
    # blink_color((255, 255, 0), 1)
    # blink_color((255, 0, 50), 1)
    
    # one_pixel_fill(0, (0, 255, 0), 1)
    # fill_circle(Day.monday, [(0, 255, 0), (255, 0, 0), (0, 0, 255), (100, 50,0)])
    # fill_circle(Day.friday, [(0, 255, 0), (255, 0, 100), (100, 50,0)])
    # sleep(10)
    # turn_off()
    upload_day_state()