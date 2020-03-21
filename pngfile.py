import os
from chunks_service import ChunksService

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
        print(" FILE INFO ".center(50, "-"))
        print("---> PATH:", self.path)
        print("---> EXTENSION: PNG")
        print("---> SIZE:", self.size, "bytes")
        print("".center(50, "-"))
        print("")
        