from store.show_store import show_store
import keyboard

def store () :
    while True :

        show_store()
        print('in store.py')

        new_key_pressed = keyboard.read_key()

        if new_key_pressed == "esc" :
            return -1
        if new_key_pressed == "1" :
            return 1
        if new_key_pressed == "2" :
            return 2
        if new_key_pressed == "3" :
            return 3