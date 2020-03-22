import os
from png_handler import PNG_handler

if __name__ == "__main__":
    file_path = input("Enter the path of your file: ")
    png_handler = PNG_handler(file_path)
    
    os.system('clear')
    png_handler.display_file_info()
    png_handler.display_chunks_type()
    png_handler.display_chunks_info()
    png_handler.display_file()


