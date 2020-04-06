from constants import TextColors
from model.base_chunk import baseCHUNK

class IENDchunk (baseCHUNK):
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        print("     > EMPTY")
 