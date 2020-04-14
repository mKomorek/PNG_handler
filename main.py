import os
import sys 
from png_handler import PNG_handler
from constants import TextColors

def submenu(png_handler):

    choice = input("""
    F: Display file information
    D: Display chunk types 
    C: Display chunk informations 
    K: Display file
    R: Display file from reconstructed IDAT chunks
    T: Perform DFT and display output
    S: Clear file and save   
    N: Back to menu \n \n"""
    + TextColors.setValueColor("""    > Your choice: """))

     
    if choice == "F" or choice =="f":
        os.system('clear') 
        png_handler.display_file_info()

    elif choice == "D" or choice =="d":
        os.system('clear')
        png_handler.display_chunks_type()

    elif choice=="C" or choice=="c":
        os.system('clear')
        png_handler.display_chunks_info()
    
    elif choice=="K" or choice=="k":
        os.system('clear')
        png_handler.display_file()

    elif choice=="R" or choice=="r":
        os.system('clear')
        png_handler.display_from_reconstructed_idats()
    
    elif choice=="T" or choice=="t":
        os.system('clear')
        png_handler.display_fourier_transform()
    
    elif choice=="S" or choice=="s":
        os.system('clear')
        png_handler.create_clean_file()

    elif choice=="N" or choice=="n":
        os.system('clear')
        return 1 
    else:
        os.system('clear')
        print("You must only select either F,D,C,K,T,N.")
        print("Please try again")
    submenu(png_handler)

def menu():
    os.system('clear')
    print(TextColors.BOLD + TextColors.HEADER + "MAIN MENU".center(50, "-") + TextColors.ENDC)

    choice = input("""
    P: Path to input file    
    Q: Quit \n \n""" 
    + TextColors.setValueColor("""    > Your choice: """))

    if choice == "P" or choice =="p":
        os.system('clear')
        file_path = input("Path: ")
        png_handler = PNG_handler(file_path)
        submenu(png_handler)
    elif choice == "Q" or choice =="q":
        return 1
    else:
        print("You must only select either P,Q.")
        print("Please try again")
    menu()

if __name__ == "__main__":
    menu()

