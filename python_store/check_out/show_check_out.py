from check_out.print_cart import print_cart
import os

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_check_out (cart) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + 'CHECK OUT')
    print()
    print(' '*10 + "[1] CHECK OUT")
    print(' '*10 + "[0] BACK")
    print()

    # แสดงข้อมูลในตะกร้า
    print_cart(cart)
    
    print()
    print( "="*36)