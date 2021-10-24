from menu.show.show_delete_menu import show_delete_menu
from menu.file.write_menu_file import write_menu_file

def delete_menu (menu_list) :
    if len(menu_list) > 0 :
        delete_index = show_delete_menu(menu_list)
        menu_list.pop(delete_index)
        write_menu_file(menu_list)