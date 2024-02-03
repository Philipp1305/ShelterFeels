from pn532.pn532.api import PN532

from dataclasses import dataclass
from config import nfc_to_emotion
from neo_pixel import fill_circle
from datetime import datetime

@dataclass
class NFCHandler:    
    nfc = PN532()
    nfc.setup()

    def read_single(self):
        return ''.join([str(x) for x in self.nfc.read()])


def read_emotion_from_nfc():
    nfc = NFCHandler()
    read_num = nfc.read_single()
    print(read_num)
    try:
        return nfc_to_emotion[read_num]
    except KeyError:
        print("TOKEN WAS NOT ASSIGNED")
        return None

if __name__ == "__main__":
    nfc = NFCHandler()
    # print(nfc.read_single())
    print(read_emotion_from_nfc())