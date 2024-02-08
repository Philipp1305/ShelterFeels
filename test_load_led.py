from time import sleep
from shelterfeels.nfc_led.neo_pixel import load_state, turn_off

if __name__ == "__main__":
    load_state()
    sleep(5)
    turn_off()
    