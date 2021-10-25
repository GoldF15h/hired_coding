from menu.show.show_search_menu import show_search_menu
from get_user_input import get_user_input

def search_menu (menu_list) :
    if len(menu_list) > 0 :
        while True :
            print("ENTER NAME TO SEARCH : ",end='')
            # รับข้อความที่ค้นหา
            inp = input()
            # แสดงผลการค้นหา
            show_search_menu(menu_list,inp)
            # รับ input
            new_key_pressed = get_user_input()

            if new_key_pressed == '0' :
                return
