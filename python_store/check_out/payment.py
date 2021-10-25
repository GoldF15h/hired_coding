def payment (cart) :
    # รวมราคาสินค้า
    s = 0
    for i in range(len(cart)) :
        s += cart[i][1] * cart[i][2]
    
    # รับจำนวนเงินที่จ่าย
    print("ENTER PAY AMOUNT : ",end='')
    inp = input()
    # ตรวจสอบว่าสามารถจ่ายได้หรือไม่
    while not( inp.isnumeric() and int(inp) >= s ) :
        print("ERROR PLEASE REENTER : ",end='')
        inp = input()
    inp = int(inp)

    # แสดงเงินทอน
    print("YOU GOT A CHANGE : ",abs(s - inp),'฿')
    print("PRESS ENTER TO EXIT ..")
    _ = input()