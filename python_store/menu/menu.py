from menu.sub_menu.add_to_cart import add_to_cart
from menu.sub_menu.add_new_menu import add_new_menu
from menu.sub_menu.delete_menu import delete_menu
from menu.sub_menu.search_menu import search_menu
from menu.file.read_menu_file import read_menu_file
from menu.file.write_menu_file import write_menu_file
from menu.show.show_menu import show_menu
from get_user_input import get_user_input

def menu() :

    cart = []

    while True :
        menu_list = read_menu_file()
        show_menu(menu_list)
        new_key_pressed = get_user_input()

        if new_key_pressed == "1" :
            add_to_cart(menu_list,cart)

        if new_key_pressed == "2" :
            add_new_menu(menu_list)

        if new_key_pressed == "3" :
            search_menu(menu_list)

        if new_key_pressed == "4" :
            delete_menu(menu_list)

        if new_key_pressed == "0" :
            write_menu_file(menu_list)
            return 0
