from cart.print.print_cart_item import print_cart_item
import os

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_cart (cart) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')
    # print(cart)
    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + "CART")
    print()
    print(" "*10+"[1] ADD ITEM")
    print(" "*10+"[2] REMOVE ITEM")
    print(" "*10+"[3] CLEAR CART")
    print(" "*10+"[0] BACK")
    print()
    
    # แสดงของในตะกร้า
    print_cart_item(cart)

    print()
    print( "="*36)

    