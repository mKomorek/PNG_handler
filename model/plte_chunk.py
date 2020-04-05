class PLTEchunk :
    def __init__(self, length, data, crc):
        self.length = int.from_bytes(length, byteorder='big')
        self.type = "PLTE"
        self.data = data
        self.crc = crc
        self.data_parser()

    def data_parser(self):
        self.paletes = [(self.data[i], self.data[i+1], self.data[i+2]) for i in range(0, self.length, 3)]

    def display_info(self):
        print()
        print("---> CHUNK LENGHT: ", self.length)
        print("---> CHUNK TYPE: PLTE")
        print("---> CHUNK CRC: ", self.crc) # wyświetlenie CRC
        print("---> CHUNK DATA: ")
        for palete in self.paletes:
            print("     > PALLETE ENTRY: ", palete)
