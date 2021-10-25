def write_cart_file (cart) :
    # ที่อยู่ของไฟล์
    f = open('cart\cart.txt','w')
    # แปลง list เป็น string เพื่อเขียน
    str_to_write = []
    if len(cart) != 0 :
        for i in range(len(cart)) :
            str_to_write.append(cart[i][0] + ' ' + str(cart[i][1]) + ' ' + str(cart[i][2]))
        str_to_write = ','.join(str_to_write)
        f.write(str_to_write)
    else :
        f.write('')
    f.close()