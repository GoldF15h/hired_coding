from check_out.show_check_out import show_check_out
from get_user_input import get_user_input

def check_out() :
    while True :
        show_check_out()
        print('in check_out.py')

        new_key_pressed = get_user_input()

        if new_key_pressed == "0" :
            return 0
