import os
from menu.print.print_menu_list import print_menu_list

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_menu (menu_list) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + '[1] ADD TO CART')
    print(' '*10 + '[2] ADD NEW MENU')
    print(' '*10 + '[3] SEARCH MENU')
    print(' '*10 + '[4] DELETE MENU')
    print(' '*10 + '[0] BACK')
    print()

    print_menu_list(menu_list)

    print()
    print( "="*36)