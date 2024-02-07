from shelterfeels.nfc_led.config import nfc_to_emotion
from shelterfeels.nfc_led.neo_pixel import fill_circle

from pn532.pn532.api import PN532
from dataclasses import dataclass


@dataclass
class NFCHandler: 
    try:   
        nfc = PN532()
        nfc.setup()
    except Exception:
        print("BAD NFC POORLY CONNECTED")
        nfc = None

    def read_single(self):
        if self.nfc is None:
            raise Exception("NFC READER NOT CONNECTED")
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