import os
from get_input import get_input

def checkout() :
    while True :
        
        show_checkout()

        inp = get_input()
        if inp == 0 :
            return 

def show_checkout() :
    os.system('cls')
    print("THIS IS CHECKOUT")
    print('[0] BACK')