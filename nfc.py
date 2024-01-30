from pn532.pn532.api import PN532

from dataclasses import dataclass

@dataclass
class NFC:    
    nfc = PN532()
    nfc.setup()

    def read_single(self):
        return self.nfc.read()


nfc = NFC()
