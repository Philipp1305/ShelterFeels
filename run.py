from datetime import datetime
from threading import Thread

from shelterfeels.gui import start_window
from shelterfeels.nfc_led.neo_pixel import load_state, turn_off, upload_day_state


def run():
    """this function exists purely for conveniently starting the application"""
    # while True:
    weekday = str(datetime.today().weekday())
    upload_day_state(weekday, [])
    Thread(target=load_state()).start()
    start_window()
    turn_off()


if __name__ == "__main__":
    run()
