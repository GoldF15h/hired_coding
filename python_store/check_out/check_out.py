from check_out.show_check_out import show_check_out
import keyboard

def check_out() :
    while True :
        show_check_out()
        print('in check_out.py')

        new_key_pressed = keyboard.read_key()

        if new_key_pressed == "0" :
            return 0
