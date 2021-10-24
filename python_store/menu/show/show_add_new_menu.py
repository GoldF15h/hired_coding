import os

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_add_new_menu (menu_list) :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print("ADD TO CART")
    print()
    print( "="*36)


    print('ENTER NAME : ',end='')
    name = input()

    print('ENTER AMOUNT : ',end='')
    amount = input()
    while not amount.isnumeric() :
        print("ERROR PLEASE ENTER INTIGER : ",end='')
        amount = input()
    amount = int(amount)

    print('ENTER PRICE : ',end='')
    price = input()
    while not price.isnumeric() :
        print("ERROR PLEASE ENTER INTIGER : ",end='')
        price = input()
    price = int(price)

    return [name,amount,price]

