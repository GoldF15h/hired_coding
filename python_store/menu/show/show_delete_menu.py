import os
from menu.print.print_menu_list import print_menu_list

def show_delete_menu (menu_list) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + 'DELETE MENU')
    print()
    
    print_menu_list(menu_list)

    print()
    print( "="*36)

    print("ENTER MENU THAT YOU WANT TO DELETE : ",end='')
    # รับข้อมูลการลบ
    inp = input()
    # ตรวจสอบข้อมูลว่าถูกต้องหรือไม่
    while not ( inp.isnumeric() and int(inp) < len(menu_list) and int(inp) >= 0 ) :
        print("ERROR PLEAS REENTER : ",end='')
        inp = input()
    inp = int(inp)

    return inp
