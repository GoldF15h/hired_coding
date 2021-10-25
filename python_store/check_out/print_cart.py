from cart.print.get_cart_detail import get_cart_detail

def print_cart (cart) :
    # เช็คว่าตะกร้าว่างหรือไม่
    if len(cart) > 0 :
        s = 0
        # แสดงของมูลในตะกร้า
        for i in range(len(cart)) :
            # แปลง list เป็น string
            print('No.',i,',',get_cart_detail(cart[i]))
            # เพิ่มยอดรวม
            s += cart[i][1] * cart[i][2]
        print()
        # แสดงยอดรวม
        print(' '*10 + "TOTAL PRICE : " , s , "฿")
    else :
        print(' '*10 + "YOUR CART IS EMPTY!")
