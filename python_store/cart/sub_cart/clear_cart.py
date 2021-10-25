from cart.file.write_cart_file import write_cart_file
from menu.file.write_menu_file import write_menu_file

def clear_cart (menu_list,cart) :
    # วิ่ง for เอาของไปคืน menu
    for i in range(len(cart)) :

        # หาของในเมนู ถ้าไม่มีให้นำไปต่อท้าย
        isFound = False
        for j in range(len(menu_list)) :
            if menu_list[j][0] == cart[i][0] :
                menu_list[j][1] += cart[i][1]
                isFound = True
                break

        if not isFound :
            menu_list.append(cart[i][::])
        
    # บันทึกตะกร้า
    write_cart_file([])
    # บันทึกเมนู
    write_menu_file(menu_list)