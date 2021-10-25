from menu.print.get_menu_detail import get_menu_detail

def print_menu_list(menu_list) :

    # ตรวจสอบว่ามีเมนูหรือไม่
    if len(menu_list) > 0 :
        print(' '*5,'MENU')
        # แสดงรายละเอียดของเมนู
        for i in range(len(menu_list)) :
            # นำเมนูไปแปลงเป็น str
            print('No.',i,',',get_menu_detail(menu_list[i]))
    else :
        print(' '*5,"MENU LIST IN EMPTY!")