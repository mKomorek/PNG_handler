class Chunk:
    def __init__(self, length, sort, crc):
        self.length = length
        self.type = sort
        self.crc = crc

    def info(self):
        print("CHUNK INFO".center(50,'-'))
        print("---> LENGTH:", self.length, "bytes")
        print("---> TYPE:", self.type)
        print("---> CRC: ", ) # dont know how display