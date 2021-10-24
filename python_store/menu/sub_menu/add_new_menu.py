from menu.show.show_add_new_menu import show_add_new_menu
from menu.file.write_menu_file import write_menu_file

def add_new_menu (menu_list) :
    new_menu = show_add_new_menu(menu_list)
    menu_list.append(new_menu)
    write_menu_file(menu_list)