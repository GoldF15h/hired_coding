from cart.show.show_remove_item import show_remove_item
from cart.file.write_cart_file import write_cart_file
from menu.file.write_menu_file import write_menu_file

def remove_item (menu_list,cart) :
    if len(cart) > 0 :
        # แสดงหน้า ui ให้กับ user
        menu_list,cart = show_remove_item(menu_list,cart)
        # บันทึกเมนู
        write_menu_file(menu_list)
        # บันทึกไฟล์
        write_cart_file(cart)