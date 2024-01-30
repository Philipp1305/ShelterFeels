from time import sleep

import board
import neopixel

# LED control
pixels = neopixel.NeoPixel(board.D18, 84)

pixels.fill((0, 255, 0))
pixels.show()                
sleep(1)

pixels.fill((0,0,0))
pixels.show()
sleep(1)