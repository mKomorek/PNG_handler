import cv2
import numpy as np
from matplotlib import pyplot as plt

class FourierPlot:
    def __init__(self, path):
        self.path = path
        self.img = ~cv2.imread(self.path,0) 
        
    def show(self):
        f = np.fft.fft2(self.img) #procesing image
    
        fshift = np.fft.fftshift(f) # move (0,0) point of 2D plot to center of image for easyer analis 
        mag = 20*np.log(np.abs(fshift)) # magnitude of fraquecies (log is for better contrast)
        mag = np.asarray(mag,dtype=np.uint8) # converting to uint8 for matplotlib
           
        phase = np.angle(fshift)
        phase = np.asarray(phase,dtype=np.uint8)
           
        plt.subplot(131),plt.imshow(self.img, cmap = 'gray') 
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
            
        plt.subplot(132),plt.imshow(mag, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
            
        plt.subplot(133),plt.imshow(phase, cmap = 'gray')
        plt.title('Phase Spectrum'), plt.xticks([]), plt.yticks([])
            
        plt.show()

    def show_compare(self):
        f = np.fft.fft2(self.img) #procesing image
        fshift = np.fft.fftshift(f) # move (0,0) point of 2D plot to center of image for easyer analis 
        mag = 20*np.log(np.abs(fshift)) # magnitude of fraquecies (log is for better contrast)
        mag = np.asarray(mag,dtype=np.uint8) # converting to uint8 for matplotlib
        
        phase = np.angle(fshift)
        phase = np.asarray(phase,dtype=np.uint8)
        
        inv=np.fft.ifft2(f)

        plt.subplot(121),plt.imshow(self.img, cmap = 'gray') 
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        
        plt.subplot(122),plt.imshow( np.asarray(inv, dtype=np.uint8), cmap = 'gray')
        plt.title('Transformed And Inverted Image'), plt.xticks([]), plt.yticks([])
        plt.show()
