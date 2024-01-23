from time import sleep
from gpiozero import LED
import nfc

import board
import neopixel


# LED control
pixels = neopixel.NeoPixel(board.D18, 7)
clf_obj = nfc.ContactlessFrontend()

# def read_nfc():
#     tag = clf_obj.connect(rdwr={'on-connect': lambda tag: False})
#     return tag.identifier.hex()

def main():
    print("Hello!")

    try:
        while True:
            # uid = read_nfc()
            uid = ''
            print(f"UID: {uid}")

            # TODO: handle different chip ids
            if uid == "":
                pixels.fill((0, 255, 0))
                pixels.show()                
                sleep(1)

                pixels.fill((0,0,0))
                pixels.show()
                sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        clf_obj.close()

if __name__ == "__main__":
    main()
