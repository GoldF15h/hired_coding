import os

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_store ():

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print( " " * front_spacing + "[1]   MENU" )
    print( " " * front_spacing + "[2]   MANAGE CART" )
    print( " " * front_spacing + "[3]   CHECK OUT" )
    print( " " * front_spacing + "[ESC] EXIT" )
    print()
    print( "="*36)