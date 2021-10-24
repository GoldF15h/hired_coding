from menu.print.print_search_menu_list import print_search_menu_list
import os

def show_search_menu (menu_list,search) :
    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()

    print(" "*5,"[0] BACK")
    print()

    print_search_menu_list(menu_list,search)

    print()
    print( "="*36)

    