from cart.print.get_cart_detail import get_cart_detail

def print_cart_item (cart) :
    # เช็คว่าตะกร้าว่างหรือไม่
    if len(cart) > 0 :
        for i in range(len(cart)) :
            # แปลง list[index] เป็น string
            print( "No.",i,get_cart_detail(cart[i]))
    else :
        print(' '*5,"CART IS EMPTY!")