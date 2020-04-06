import os
import sys 
from png_handler import PNG_handler

def submenu(png_handler):

    choice = input("""
                            F: Display file information
                            D: Display chunk types 
                            C: Display chunk informations 
                            K: Display file
                            T: Perform DFT and display output  
                            N: Back to menu

Your choice: """)

     
    if choice == "F" or choice =="f": 
        png_handler.display_file_info()
    elif choice == "D" or choice =="d":
        png_handler.display_chunks_type()
    elif choice=="C" or choice=="c":
        png_handler.display_chunks_info()
    
    elif choice=="K" or choice=="k":
        png_handler.display_file()
    
    elif choice=="T" or choice=="t":
        png_handler.display_fourier_transform()
    elif choice=="N" or choice=="n":
        return 1 
    else:
        print("You must only select either F,D,C,K,T,N.")
        print("Please try again")
    submenu(png_handler)
def menu():
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      P: Path to input file    
                      Q: Quit

Your choice: """)

    if choice == "P" or choice =="p":
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

