from check_out.show_check_out import show_check_out
from cart.file.read_cart_file import read_cart_file
from cart.file.write_cart_file import write_cart_file
from check_out.payment import payment
from get_user_input import get_user_input

def check_out() :
    while True :
        # อ่านไฟล์ตะกร้า
        cart = read_cart_file()
        # แสดงหน้า ui กับ user
        show_check_out(cart)
        # รับข้อมูลจาก user
        new_key_pressed = get_user_input()
        # เลือกจ่ายเงิน
        if new_key_pressed == "1" :
            # การจ่ายเงิน
            payment(cart)
            # บันทึกตะกร้า
            write_cart_file([])
            # ย้อนกลับ
            return 0
        # ย้อนกลับ
        if new_key_pressed == "0" :
            return 0
