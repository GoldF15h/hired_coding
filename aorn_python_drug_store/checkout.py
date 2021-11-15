import os
from get_input import get_input
from cart import show_cart_list_info
from mange_file import read_cart
from mange_file import write_cart

err_msg = 'ENTER THE IN PUT WITHIN RANGE : '

def show_checkout() :
    os.system('cls')
    print("THIS IS CHECKOUT")
    show_cart_list_info()
    print('[1] CHECK OUT')
    print('[0] BACK')

def payment() :
    os.system('cls')
    print("PAYMENT")
    totol_price = show_cart_list_info()
    pay_price = input("ENTER YOUR PAYMENT : ")
    while not( pay_price.isnumeric() and totol_price <= int(pay_price) ):
        pay_price = input(err_msg)
    pay_price = int(pay_price)
    receipt = create_receipt(pay_price)
    os.system('cls')
    print(receipt)
    input('PRESS ENTER TO CONTINUE .....')
    write_cart([])

    f = open("receipt.txt", "a")
    f.write('\n\n\n' + receipt)
    f.close()

def create_receipt (pay_price) :
    cart_list = read_cart()
    total_price = 0
    for i in range(len(cart_list)) :
        total_price += cart_list[i]['price'] * cart_list[i]['amount']

    receipt = ''
    receipt += '========= KMITL DRUG STORE =========' + '\n'
    receipt +=  '\n'
    receipt += 'AMOUNT       NAME           SUBTOTAL' + '\n'
    
    for i in range(len(cart_list)) :
        if len(cart_list[i]['name']) <= 14 :
            receipt += str(cart_list[i]['amount']) + ' '*(10 - len(str(cart_list[i]['amount']))) + cart_list[i]['name'] + ' '*(18-len(cart_list[i]['name'])) + str(cart_list[i]['price']*cart_list[i]['amount'] ) + '\n'
        else :
            receipt += str(cart_list[i]['amount']) + ' '*(10 - len(str(cart_list[i]['amount']))) + cart_list[i]['name'][:14:] + '    ' + str(cart_list[i]['price']*cart_list[i]['amount'] ) + '\n'
            for j in range(14,len(cart_list[i]['name']),14) :
                receipt += '          ' + cart_list[i]['name'][j:j+14:] + '\n'

    receipt +=  '\n'
    receipt += '====================================' + '\n'
    receipt += 'TOTAL PRICE : ' + str(total_price) + '\n'
    receipt += 'CASH : ' + str(pay_price) + '\n'
    receipt += '**CHANGE** : ' + str(pay_price - total_price) + '\n'
    receipt += '====================================' + '\n'

    # print(receipt)
    # input('....')

    return receipt

def checkout() :
    while True :
        
        show_checkout()

        inp = get_input()
        if inp == 0 :
            return 
        elif inp == 1 :
            payment()
            # create_receipt(2000)