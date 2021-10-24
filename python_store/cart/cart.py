from cart.show_cart import show_cart
from get_user_input import get_user_input

def cart() :
    while True :
        show_cart()
        print('in cart.py')

        new_key_pressed = get_user_input()

        if new_key_pressed == "0" :
            return 0
