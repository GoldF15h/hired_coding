from store.store import store
from menu.menu import menu
from cart.cart import cart
from check_out.check_out import check_out

# กำหนด 
# state  0  -> หน้าหลัก
# state  1  -> เมนู
# state  2  -> จัดการตะกร้า
# state  3  -> คิดเงิน
# state  -1 -> ออก

# สร้างตัวแปรเก็บค่า state ปัจจุบันของร้านค้า
current_state = 0

# สร้าง dict สำหรับเก็บ function สำหรับเมนูต่าง ๆ
switch = {  
    0 : store,
    1 : menu,
    2 : cart,
    3 : check_out
}

# ทำงานคำสั่งและเปลี่ยน current_state ไปเรื่อย ๆ ตามแต่ state ของโปรแกรม
while True :

    try :
        current_state = switch[current_state]()
        if current_state == -1 :
            break
    except Exception as e:
        current_state = 0
        print(e)
        _ = input()