import os

# กำหนดตัวแปรสำหรับเว้นระยะห่างด้านหน้าของเมนู
front_spacing = 11

def show_menu () :

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print('MENU')
    print()
    print( "="*36)