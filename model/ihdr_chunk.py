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

class IHDRchunk :
    def __init__(self, length, data, crc):
        self.length = int.from_bytes(length, byteorder='big')
        self.type = "IHDR"
        self.crc = crc
        self.chunk_data = data
        self.data_parser()

    def data_parser(self):
        if self.length != 13:
            print("CHUNK IS BROKEN!")
            return
        else:
            self.width = int.from_bytes(self.chunk_data[0:4], byteorder = 'big')
            self.height = int.from_bytes(self.chunk_data[4:8], byteorder = 'big')
            self.bit_depth = int.from_bytes(self.chunk_data[8:9], byteorder = 'big')
            self.color_type = int.from_bytes(self.chunk_data[9:10], byteorder = 'big')
            self.compression_method = int.from_bytes(self.chunk_data[10:11], byteorder = 'big')
            self.filter_method = filter_type_switch(int.from_bytes(self.chunk_data[11:12], byteorder = 'big'))
            if int.from_bytes(self.chunk_data[11:12], byteorder = 'big') == 0:
                self.interlace_methode = "no interlace"
            else:
                self.interlace_methode = "Adam7 interlace"
    
    def display_info(self):
        print()
        print("---> CHUNK LENGHT: ", self.length)
        print("---> CHUNK TYPE: IHDR")
        print("---> CHUNK CRC: ", self.crc) # wyświetlenie CRC
        print("---> CHUNK DATA: ")
        print("     > WIDTH: ", self.width)
        print("     > HEIGHT: ", self.height)
        print("     > BIT DEPTH: ", self.bit_depth)
        print("     > COLOR TYPE: ", color_type_switch(self.color_type))
        print("     > COMPRESSION METHOD: ", self.compression_method)
        print("     > FILTER METHOD: ", self.filter_method)
        print("     > INTERLACE METHODE: ", self.interlace_methode)
        print()
