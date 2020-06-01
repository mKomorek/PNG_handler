import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pngfile import PNGfile
from chunks_service import ChunksService
from fourierplot.fourierplot import FourierPlot

class PNG_handler:
    
    def __init__(self, file_path):
        self.path = file_path
        self.png_file = PNGfile(file_path)
        self.chunks_service = ChunksService(self.png_file.data)
        self.fourier_plot = FourierPlot(file_path)
    
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

    def display_fourier_transform(self):
        self.fourier_plot.show_compare()
        self.fourier_plot.show()

    def display_from_reconstructed_idats(self):
        self.chunks_service.display_from_IDATs()
    
    def create_clean_file(self):
        file_name = input("Enter the name of file: ")
        self.chunks_service.create_clean_file(file_name)

    def make_encryption_ecb(self):
        self.chunks_service.make_encryption_ecb()

    def make_encryption_cbc(self):
        self.chunks_service.make_encryption_cbc()
