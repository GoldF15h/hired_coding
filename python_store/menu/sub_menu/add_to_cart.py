from menu.show.show_add_to_cart import show_add_to_cart
from menu.file.write_menu_file import write_menu_file
from get_user_input import get_user_input

def add_to_cart (menu_list,cart) :
    if len(menu_list) > 0 :
        menu_list = show_add_to_cart(menu_list,cart)
        write_menu_file(menu_list)