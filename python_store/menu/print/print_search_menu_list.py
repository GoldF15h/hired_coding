from menu.print.get_menu_detail import get_menu_detail

def print_search_menu_list (menu_list,search) :
    print(" "*5+" SEARCH RESAULT FOR : " + '" ' +search + ' "')
    # วิ่งหาข้อความที่ค้นหา
    for i in range(len(menu_list)) :
        # ตรวจสอบว่าใช่คำที่ค้นหาหรือไม่
        if search in menu_list[i][0] :
            print('No.',i,',',get_menu_detail( menu_list[i] ))
