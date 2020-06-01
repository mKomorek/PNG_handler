import zlib 
import matplotlib.pyplot as plt
import numpy as np
from constants import TextColors
from model.base_chunk import baseCHUNK
from RSA.rsa import RSA

def get_byte_per_pixel(argument):
    switcher = {
        0: 1,
        2: 3,
        3: 1,
        4: 2,
        6: 4,
    }
    return switcher.get(argument, "Not found")

class IDATchunk (baseCHUNK) :
    def __init__(self, length, chunkType, data, crc, width, color_type):
        super().__init__(length, chunkType, data, crc)
        self.width = width
        self.color_type = color_type
        self.bytes_per_pixel = get_byte_per_pixel(color_type)
        self.initRsa()

    def initRsa(self):
        data = self.data
        key_size = 1024
        step = key_size // 8 - 1
        data = [data[i:i+step] for i in range(0, len(data), step)]
        data = [bytearray(slice) for slice in data]
        data_sizes = [int.from_bytes(slice, 'big') for slice in data]
        self.rsa = RSA(max(data_sizes), key_size)
        
    def data_parser(self):
        self.data = zlib.decompress(self.data)
        self.height = (int)( len(self.data) / (1 + self.width*self.bytes_per_pixel) )
        self.reconstructed_data = []
        stride = self.width * self.bytes_per_pixel
        i = 0
        for r in range(self.height):
            filter_type = self.data[i]
            i += 1
            for c in range(stride):
                filt_x = self.data[i]
                i += 1
                if filter_type == 0:
                    recon_x  = filt_x
                elif filter_type == 1:
                    recon_x = filt_x + self.reconstruction_a(r, c, stride)
                elif filter_type == 2:
                    recon_x = filt_x + self.reconstruction_b(r, c, stride)
                elif filter_type == 3:
                    recon_x = filt_x + (self.reconstruction_a(r, c, stride)
                     + self.reconstruction_b(r, c, stride)) // 2
                elif filter_type == 4:
                    recon_x = filt_x + self.paeth_predictor(self.reconstruction_a(r, c, stride),
                     self.reconstruction_b(r, c, stride), self.reconstruction_c(r, c, stride))
                else:
                    raise Exception("unknown filter type: " + str(filter_type))
                self.reconstructed_data.append(recon_x & 0xff) #truncation to byte

    def paeth_predictor(self, a, b, c):
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)
        if pa <= pb and pa <= pc:
            Pr = a
        elif pb <= pc:
            Pr = b
        else:
            Pr = c
        return Pr

    def reconstruction_a(self, r, c, stride):
        if c >= self.bytes_per_pixel:
            return self.reconstructed_data[r * stride + c - self.bytes_per_pixel]
        else:
            return 0

    def reconstruction_b(self, r, c, stride):
        if r > 0:
            return self.reconstructed_data[(r-1) * stride + c]
        else:
            return 0

    def reconstruction_c(self, r, c, stride):
        if r > 0 and c >= self.bytes_per_pixel:
            return self.reconstructed_data[(r-1) * stride + c - self.bytes_per_pixel]
        else:
            return 0
    
    def apply_palette(self, palette):
        self.reconstructed_data = [pixel for pixel_i in self.reconstructed_data for pixel in palette[pixel_i]]
        self.bytes_per_pixel = 3

    def display_info(self):
        print()
        self.display_basic_info()
        print("---> CHUNK DATA: HUGE STRING OF BYTES...")
        print()

    # a special method for cbc encryption may have too large numbers which by 
    # default will be projected by python onto some other type
    def display_image_from_recostrucrion_data_encryption_cbc(self):
        temp = list(map(float, self.reconstructed_data))
        plt.imshow(np.array(temp).reshape((self.height, self.width, self.bytes_per_pixel)))
        plt.show()

    def display_image_from_recostrucrion_data(self):
        plt.imshow(np.array(self.reconstructed_data).reshape((self.height, self.width, self.bytes_per_pixel)))
        plt.show()

    def encryption_ecb(self):
        self.reconstructed_data = self.rsa.encryption_ecb(self.reconstructed_data)

    def decryption_ecb(self):
        self.reconstructed_data = self.rsa.decryption_ecb(self.reconstructed_data)

    def encryption_cbc(self):
        self.reconstructed_data = self.rsa.encryption_cbc(self.reconstructed_data)

    def decryption_cbc(self):
        self.reconstructed_data = self.rsa.decryption_cbc(self.reconstructed_data)