def read_menu_file () :
    # ที่อยู่ของเมนู
    PATH = 'menu\menu.txt'

    # เปิดไฟล์
    f = open(PATH,'r')

    # อ่านไฟล์
    text = f.read()

    # เช็คหากเป็นไฟล์เปล่า
    if len(text) == 0 :
        return []
        
    # แยกตัวเมนู และทำการเก็บไว้ใน list
    menu_list = text.split(',')

    # แปลงเมนูให้อยู่ในรูปแบบที่ใช้งาน
    for i in range(len(menu_list)) :
        try :
            tmp = menu_list[i].split()
            menu_list[i] = [tmp[0],int(tmp[1]),int(tmp[2])]
        except :
            return []

    # ปิดไฟล์
    f.close()

    return menu_list