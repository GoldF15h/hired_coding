from menu.show_menu import show_menu
import keyboard

def menu() :
    while True :
        show_menu()
        print('in menu.py')

        new_key_pressed = keyboard.read_key()

        if new_key_pressed == "0" :
            return 0
