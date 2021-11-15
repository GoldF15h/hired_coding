from get_input import get_input
from mange_file import read_cart
from mange_file import write_cart

import os

def show_cart () :
    os.system('cls')
    print("THIS IS CART")
    show_cart_list_info()
    print("[1] ADD TO CART")
    print("[2] REMOVE FROM CART")
    print("[3] CLEAR CART")
    print("[0] BACK")

def show_cart_list_info () :
    cart_list = read_cart()
    total_price = 0
    for i in range(len(cart_list)) :
        total_price += cart_list[i]['price'] * cart_list[i]['amount']
        print( get_cart_info(cart_list[i]))
    print('TOTAL PRICE :',total_price)

def get_cart_info(x) :
    return 'NAME : ' + x['name'] + ' , PRICE ' + str(x['price']) + ' , AMOUNT : ' + str(x['amount'])

def cart() :
    while True :

        show_cart()
        inp = get_input()
        if inp == 0 :
            return 
