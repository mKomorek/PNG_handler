from model.base_chunk import baseCHUNK
from constants import TextColors

class tIMEChunk (baseCHUNK):
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)
        self.data_parser()

    def data_parser(self):
        self.year = int.from_bytes(self.data[0:2], byteorder='big')
        self.month = int.from_bytes(self.data[2:3], byteorder='big')
        self.day = int.from_bytes(self.data[3:4], byteorder='big')
        self.hour = int.from_bytes(self.data[4:5], byteorder='big')
        self.minute = int.from_bytes(self.data[5:6], byteorder='big')
        self.second = int.from_bytes(self.data[6:7], byteorder='big')

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        print("     > YEAR: ", TextColors.setValueColor(str(self.year)))
        print("     > MONTH: ", TextColors.setValueColor(str(self.month)))
        print("     > DAY: ", TextColors.setValueColor(str(self.day)))
        print("     > HOUR: ", TextColors.setValueColor(str(self.hour)))
        print("     > MINUTE: ", TextColors.setValueColor(str(self.minute)))
        print("     > SECOND: ", TextColors.setValueColor(str(self.second)))
        print()

class cHRMChunk (baseCHUNK):
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)
        self.data_parser()

    def data_parser(self):
        self.white_point_x = int.from_bytes(self.data[0:4], byteorder='big')/100000
        self.white_point_y = int.from_bytes(self.data[4:8], byteorder='big')/100000
        self.red_x = int.from_bytes(self.data[8:12], byteorder='big')/100000
        self.red_y = int.from_bytes(self.data[12:16], byteorder='big')/100000
        self.green_x = int.from_bytes(self.data[16:20], byteorder='big')/100000
        self.green_y = int.from_bytes(self.data[20:24], byteorder='big')/100000
        self.blue_x = int.from_bytes(self.data[24:28], byteorder='big')/100000
        self.blue_y = int.from_bytes(self.data[28:32], byteorder='big')/100000

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        print("     > WHITE POINT X: ", TextColors.setValueColor(str(self.white_point_x)))
        print("     > WHITE POINT Y: ", TextColors.setValueColor(str(self.white_point_y)))
        print("     > RED X: ", TextColors.setValueColor(str(self.red_x)))
        print("     > RED Y: ", TextColors.setValueColor(str(self.red_y)))
        print("     > GREEN X: ", TextColors.setValueColor(str(self.green_x)))
        print("     > GREEN Y: ", TextColors.setValueColor(str(self.green_y)))
        print("     > BLUE X: ", TextColors.setValueColor(str(self.blue_x)))
        print("     > BLUE Y: ", TextColors.setValueColor(str(self.blue_y)))
        print()

class gAMAChunk (baseCHUNK):
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)
        self.data_parser()

    def data_parser(self):
        self.gamma_value = int.from_bytes(self.data, "big")/100000

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        print("     > GAMMA VALUE: ", TextColors.setValueColor(str(self.gamma_value)))
        print()