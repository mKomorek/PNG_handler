from constants import TextColors
from model.base_chunk import baseCHUNK

class PLTEchunk (baseCHUNK) :
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)
        self.data_parser()

    def data_parser(self):
        self.paletes = [(self.data[i], self.data[i+1], self.data[i+2]) for i in range(0, int.from_bytes(self.length, byteorder="big"), 3)]

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        for palete in self.paletes:
            print("     > PALLETE ENTRY: ", TextColors.setValueColor(str(palete)))
        print()
