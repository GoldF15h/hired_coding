import os

def show_store ():

    # ล้างการแสดงผลของหน้าจอ
    os.system('cls')

    # แสดงผลส่วนของหน้าหลัก
    print( "="*10 + " LKB RESTAURANT " + "="*10 )
    print()
    print(' '*10 + "STORE")
    print()
    print( " " * 10 + "[1] MENU" )
    print( " " * 10 + "[2] MANAGE CART" )
    print( " " * 10 + "[3] CHECK OUT" )
    print( " " * 10 + "[0] EXIT" )
    print()
    print( "="*36)