from cart.show_cart import show_cart
import keyboard

def cart() :
    while True :
        show_cart()
        print('in cart.py')

        new_key_pressed = keyboard.read_key()

        if new_key_pressed == "0" :
            return 0
