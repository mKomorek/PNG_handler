import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pngfile import PNGfile
from chunks_service import ChunksService

class PNG_handler:
    
    def __init__(self, file_path):
        self.path = file_path
        self.png_file = PNGfile(file_path)
        self.chunks_service = ChunksService(self.png_file.data)
    
    def display_file(self):
        img = mpimg.imread(self.path)
        plt.imshow(img)
        plt.show()

    def display_file_info(self):
        self.png_file.file_info()
    
    def display_chunks_type(self):
        self.chunks_service.display_chunks_type()

    def display_chunks_info(self):
        self.chunks_service.display_chunks_info()
