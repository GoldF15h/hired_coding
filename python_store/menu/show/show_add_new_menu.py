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

    # รับชื่อเมนู
    print('ENTER NAME : ',end='')
    name = input()

    # รับจำนวนเมนู
    print('ENTER AMOUNT : ',end='')
    amount = input()
    # ตรวจสอบรูปแบบของข้อมูลว่าถูกต้องหรือไม่
    while not (amount.isnumeric() and int(amount) > 0) :
        print("ERROR PLEASE ENTER INTIGER : ",end='')
        amount = input()
    amount = int(amount)

    # รับราคา
    print('ENTER PRICE : ',end='')
    price = input()
    # ตรวจสอบรูปแบบว่าถูกต้องหรือไม่
    while not (price.isnumeric() and int(price) > 0) :
        print("ERROR PLEASE ENTER INTIGER : ",end='')
        price = input()
    price = int(price)

    return [name,amount,price]

