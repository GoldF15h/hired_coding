from store import store
from cart import cart
from checkout import checkout
from get_input import get_input
import os

state = 1

state_function = ( store , cart , checkout)

while True : 
    os.system('cls')

    print('===== WELCOME TO KMITL DRUG STORE =====')
    print('[1] STORE')
    print('[2] CART')
    print('[3] CHECKOUT')
    print('=======================================')
    inp = get_input()

    if inp == 0 :
        break

    if 1 <= inp and inp <= 3 :
        state = int(inp)
        state_function[state-1]()
    
