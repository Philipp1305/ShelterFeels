from shelterfeels.gui import start_window
from shelterfeels.nfc_led.neo_pixel import load_state, turn_off, upload_day_state
from shelterfeels.nfc_led.config import daynum_to_day
from datetime import datetime

from multiprocessing import Process


def run():
    '''this function exists purely for conveniently starting the application'''
    # while True:
    weekday = str(datetime.today().weekday())
    day = daynum_to_day[weekday]
    upload_day_state(weekday, [])
    Process(target=load_state, daemon=True).start()
    start_window()
    turn_off()


if __name__ == "__main__":
    run()
