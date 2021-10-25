from cart.show.show_cart import show_cart
from cart.file.read_cart_file import read_cart_file
from cart.sub_cart.remove_item import remove_item
from cart.sub_cart.clear_cart import clear_cart
from menu.file.read_menu_file import read_menu_file
from menu.sub_menu.add_to_cart import add_to_cart
from get_user_input import get_user_input

def cart() :
    while True :
        # อ่านไฟล์ตะกร้า
        cart = read_cart_file()
        # อ่านไฟล์เมนู
        menu_list = read_menu_file()
        # แสดงตะกร้า
        show_cart(cart)
        # รับ input จาก user
        new_key_pressed = get_user_input()

        # เพิ่มของในตะกร้า
        if new_key_pressed == "1" :
            add_to_cart(menu_list,cart)
        # ลบของออกจากตะกร้า
        if new_key_pressed == "2" :
            remove_item(menu_list,cart)
        # ล้างตะกร้า
        if new_key_pressed == "3" :
            clear_cart(menu_list,cart)
        # ย้อนกลับ
        if new_key_pressed == "0" :
            return 0
