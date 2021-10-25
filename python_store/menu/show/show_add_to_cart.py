import os
from menu.print.print_menu_list import print_menu_list

def show_add_to_cart (menu_list,cart) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print(cart)
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + 'ADD TO CART')
    print()

    print_menu_list(menu_list)

    print()
    print( "="*36)

    # รับข้อมูล index ของ list ที่จะเพิ่มในเมนู
    print("ENTER THE MENU THAT YOU WANT TO ADD : ",end='')
    ind = input()
    # เช็ค input() ว่าถูกต้องหรือไม่
    while not ( ind.isnumeric() and int(ind) < len(menu_list) and int(ind) >= 0 ) :
        print("ERROR PLEASE REENTER : ",end='')
        ind = input()
    ind = int(ind)

    # รับข้อมูลจำนวนของสินค้าที่ต้องการเพิ่ม
    print("ENTER AMOUNT : ",end='')
    amont = input()
    # เช็ค input() ว่าถูกต้องหรือไม่
    while not ( amont.isnumeric() and int(amont) <= menu_list[ind][1] and int(amont) > 0 ) :
        print("ERROR PLEASE REENTER : ",end='')
        amont = input()
    amont = int(amont)

    # ทำการ copy ข้อมูลภายใน list[index]
    new_item = menu_list[ind][::]
    new_item[1] = amont

    # หาว่ามีสินค้าในตะกร้าแล้วหรือไม่
    isFound = False
    for i in range(len(cart)) :
        if cart[i][0] == new_item[0] :
            cart[i][1] += amont
            isFound = True
            break
    if not isFound :
        cart.append( new_item )

    # ลดจำนวนของเมนูที่เหลืออยู่
    menu_list[ind][1] -= amont
    if menu_list[ind][1] <= 0 :
        menu_list.pop(ind)

    return menu_list
