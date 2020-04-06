import os
from constants import TextColors

class PNGfile:
    
    def __init__(self, path):
        self.path = path
        self.read_file()
        self.check_signature()

    def read_file(self):
        png_file = open(self.path, "rb")
        self.data = png_file.read()       
        png_file.close()
        self.size = len(self.data)
    
    def check_signature(self):
        assert self.data[:8] == b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

    def file_info(self):
        print(TextColors.BOLD + TextColors.HEADER + " FILE INFO ".center(50, "-") + TextColors.ENDC)
        print("---> PATH: ", TextColors.setValueColor(self.path))
        print("---> EXTENSION: ", TextColors.setValueColor("PNG"))
        print("---> MAGIC NUMBER: ", TextColors.setValueColor("89 50 4E 47 0D 0A 1A 0A"))
        print("---> SIZE:", TextColors.setValueColor(str(self.size)), TextColors.setValueColor("bytes"))
        print(TextColors.BOLD + TextColors.HEADER + "".center(50, "-") + TextColors.ENDC)
        print("")
        