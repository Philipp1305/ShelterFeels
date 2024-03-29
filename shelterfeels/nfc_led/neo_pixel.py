from shelterfeels.nfc_led.config import number_of_leds, number_of_led_in_circle, Day, brightness_scale, json_path, \
    daynum_to_day

from time import sleep
from typing import Union, List, Tuple
import json

import board
import neopixel

try:
    pixels = neopixel.NeoPixel(board.D18, number_of_leds)  # 84 is number of LEDs
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
        for day_num, color in colors.items():
            fill_circle(daynum_to_day[day_num], color)
    return colors


def load_state_file():
    return json.load(open(json_path, "r"))


def blink_color(color: tuple):
    if pixels is None:
        return
    pixels.fill([x * brightness_scale for x in color])
    pixels.show()
    sleep(1)

    pixels.fill((0, 0, 0))
    pixels.show()
    sleep(1)


def one_pixel_fill(led_number: int, color: tuple):
    if pixels is None:
        return
    pixels[led_number] = [x * brightness_scale for x in color]
    pixels.show()
    sleep(1)

    pixels[led_number] = 0, 0, 0
    pixels.show()
    sleep(1)


def turn_off():
    print("Turning off the lights")
    if pixels is None:
        return
    pixels.fill((0, 0, 0))
    pixels.show()


def fill_circle(circle_number: Union[int, Day], colors: List[Tuple[int, int, int]],
                number_of_led_in_circle: int = number_of_led_in_circle):
    """
    Highlights circle with given colors. 
    
    circle_number - nhumber of exact LED  or day that should be highligthed
    colors - array of RGB tuples that should be displayed. Size not more than number_of_led_in_circle
    number_of_led_in_circle - number of LED in each circle
    """
    if pixels is None:
        return
    if len(colors) == 0:
        colors = [(0, 0, 0)]
    if len(colors) > number_of_led_in_circle:
        print(f"Bad number of colors = {len(colors)}, more than number_of_led_in_circle={number_of_led_in_circle}")
        return
    if isinstance(circle_number, Day):
        circle_number = circle_number.value
    print("Filling Circle:", circle_number)
    each_color_quantity = number_of_led_in_circle // len(colors)
    divide_mod = number_of_led_in_circle % len(colors)
    right = circle_number * number_of_led_in_circle
    for num, color in enumerate(colors):
        left = right
        right += each_color_quantity
        if divide_mod and len(colors) - num <= divide_mod:
            right += 1
        print(f"color {num}/{len(colors)}, {color}, left, {left}, right, {right}, {list(range(left, right))}")
        if right > circle_number * number_of_led_in_circle + number_of_led_in_circle:
            right = circle_number * number_of_led_in_circle + number_of_led_in_circle
            print("overflow")
        for v in range(left, right):  # set color
            sleep(0.1)
            pixels[v] = [x * brightness_scale for x in color]
    pixels.show()
