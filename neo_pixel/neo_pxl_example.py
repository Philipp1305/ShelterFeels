import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 7)

pixels.fill((0, 255, 0))
pixels.show()
pixels.fill((0,0,0))
pixels.show()