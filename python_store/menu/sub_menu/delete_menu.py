from menu.show.show_delete_menu import show_delete_menu
from menu.file.write_menu_file import write_menu_file

def delete_menu (menu_list) :
    if len(menu_list) > 0 :
        # แสดงหน้า ui ให้กับ user
        delete_index = show_delete_menu(menu_list)
        # ลบเมนู
        menu_list.pop(delete_index)
        # บันทึกไฟล์
        write_menu_file(menu_list)