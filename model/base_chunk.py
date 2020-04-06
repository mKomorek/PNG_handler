from constants import TextColors

class baseCHUNK:
    def __init__(self, length, chunkType, data, crc):
        self.length = length
        self.type = chunkType
        self.data = data
        self.crc = crc

    def display_basic_info(self):
        print("---> CHUNK LENGHT: ", TextColors.setValueColor(str(int.from_bytes(self.length, byteorder="big"))))
        print("---> CHUNK TYPE: ", TextColors.setValueColor(self.type.decode()))
        print("---> CHUNK CRC: ", TextColors.setValueColor(str(self.crc)))
