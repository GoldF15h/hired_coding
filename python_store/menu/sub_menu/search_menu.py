from menu.show.show_search_menu import show_search_menu
from get_user_input import get_user_input

def search_menu (menu_list) :
    if len(menu_list) > 0 :
        while True :
            print("ENTER NAME TO SEARCH : ",end='')
            inp = input()
            show_search_menu(menu_list,inp)
            new_key_pressed = get_user_input()
            if new_key_pressed == '0' :
                return
