from cart.print.print_cart_item import print_cart_item
import os

def show_remove_item (menu_list,cart) :

    os.system('cls')

    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10,"REMOVE ITEM")
    print()
    # แสดงของในตะกร้า
    print_cart_item(cart)
    print()
    print( "="*36)

    # รับ index ที่ต้องการลบ
    print("ENTER THE NUMBER THAT YOU WANT TO REMOVE : ",end='')
    ind = input()
    # ตรวจสอบข้อมูลว่าถูกต้องหรือไม่
    while not ( ind.isnumeric() and int(ind) >= 0 and int(ind)<len(cart) ) :
        print("ERROR PLEASE REENTER : ",end='')
        ind = input()
    ind = int(ind)

    # รับจำนวนที่ต้องการลบ
    print("ENTER AMOUNT : ",end='')
    amonut = input()
    # ตรวจสอบข้อมูลว่าถูกต้องหรือไม่
    while not ( amonut.isnumeric() and int(amonut) >= 0 and int(amonut)<=cart[ind][1] ) :
        print("ERROR PLEASE REENTER : ",end='')
        amonut = input()
    amonut = int(amonut)

    # คืนของในเมนู
    isFound = False
    for i in range(len(menu_list)) :
        if menu_list[i][0] == cart[ind][0] :
            menu_list[i][1] += amonut
            isFound = True
            break
    
    # ถ้าไม่มีให้เอาไปต่อท้ายเลย
    if not isFound :
        new_item = [cart[ind][0],amonut,cart[ind][2]]
        menu_list.append(new_item)

    # ลบของออกจากตะกร้า
    cart[ind][1] -= amonut
    if cart[ind][1] <= 0 :
        cart.pop(ind)

    return menu_list,cart
    
