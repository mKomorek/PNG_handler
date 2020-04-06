from constants import TextColors
from model.base_chunk import baseCHUNK

def color_type_switch(argument):
    switcher = {
        0: "0 -> Each pixel is a grayscale sample.",
        2: "2 -> Each pixel is an R,G,B triple.",
        3: "3 -> Each pixel is a palette index; a PLTE chunk must appear.",
        4: "4 -> Each pixel is a grayscale sample, followed by an alpha sample.",
        6: "6 -> Each pixel is an R,G,B triple, followed by an alpha sample.",
    }
    return switcher.get(argument, "Not found")

def filter_type_switch(argument):
    switcher = {
        0: "0 -> None",
        1: "2 -> Sub.",
        2: "3 -> Up",
        3: "4 -> Average",
        4: "6 -> Paeth",
    }
    return switcher.get(argument, "Not found")

class IHDRchunk (baseCHUNK) :
    def __init__(self, length, chunkType, data, crc):
        super().__init__(length, chunkType, data, crc)
        self.data_parser()

    def data_parser(self):
        if int.from_bytes(self.length, byteorder="big") != 13:
            print("CHUNK IS BROKEN!")
            return
        else:
            self.width = int.from_bytes(self.data[0:4], byteorder = 'big')
            self.height = int.from_bytes(self.data[4:8], byteorder = 'big')
            self.bit_depth = int.from_bytes(self.data[8:9], byteorder = 'big')
            self.color_type = int.from_bytes(self.data[9:10], byteorder = 'big')
            self.compression_method = int.from_bytes(self.data[10:11], byteorder = 'big')
            self.filter_method = filter_type_switch(int.from_bytes(self.data[11:12], byteorder = 'big'))
            if int.from_bytes(self.data[11:12], byteorder = 'big') == 0:
                self.interlace_methode = "no interlace"
            else:
                self.interlace_methode = "Adam7 interlace"
    
    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: ")
        print("     > WIDTH: ", TextColors.setValueColor(str(self.width)))
        print("     > HEIGHT: ", TextColors.setValueColor(str(self.height)))
        print("     > BIT DEPTH: ", TextColors.setValueColor(str(self.bit_depth)))
        print("     > COLOR TYPE: ", TextColors.setValueColor(color_type_switch(self.color_type)))
        print("     > COMPRESSION METHOD: ", TextColors.setValueColor(str(self.compression_method)))
        print("     > FILTER METHOD: ", TextColors.setValueColor(self.filter_method))
        print("     > INTERLACE METHODE: ", TextColors.setValueColor(self.interlace_methode))
        print()
