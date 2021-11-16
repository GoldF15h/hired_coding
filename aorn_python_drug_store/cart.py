from get_input import get_input
from mange_file import read_cart
from mange_file import write_cart
from mange_file import read_drug
from mange_file import write_drug
from store import show_drug_list_info
from store import add_to_cart
import os

err_msg = 'ENTER THE IN PUT WITHIN RANGE : '

def show_cart () :
    os.system('cls')
    print('========== MANGE CART ==========\n')
    show_cart_list_info()
    print('\n================================\n')
    print("[1] ADD TO CART")
    print("[2] REMOVE FROM CART")
    print("[3] CLEAR CART")
    print("[0] BACK\n")


def show_cart_list_info () :
    cart_list = read_cart()
    if len(cart_list) > 0 :
        total_price = 0
        for i in range(len(cart_list)) :
            total_price += cart_list[i]['price'] * cart_list[i]['amount']
            print( i,get_cart_info(cart_list[i]))
        print('TOTAL PRICE :',total_price)
        return total_price
    else :
        print('YOUR CART IS EMPTY!!')

def get_cart_info(x) :
    return 'NAME : ' + x['name'] + ' , PRICE ' + str(x['price']) + ' , AMOUNT : ' + str(x['amount'])

def remove_from_cart():
    cart_list = read_cart()

    os.system('cls')
    print("========== REMOVE FROM CART ==========\n")
    show_cart_list_info()
    print("\n======================================\n")

    ind = input("ENTER THE INDEX THAT YOU WANT TO REMOVE : ")
    while not ( ind.isnumeric() and 0 <= int(ind) and int(ind) < len(cart_list) ) :
        ind = input(err_msg)
    ind = int(ind)

    amount = input("ENTER AMOUNT : ")
    while not ( amount.isnumeric() and int(amount) > 0 and int(amount) <= cart_list[ind]['amount'] ) :
        amount = input(err_msg)
    amount = int(amount)

    removed_item = cart_list[ind].copy()

    drug_list = read_drug()
    for i in range(len(drug_list)) :
        if drug_list[i]['name'] == removed_item['name'] :
            drug_list[i]['amount'] += amount
            removed_item = ''
            break
    
    if removed_item != '' :
        drug_list.append(removed_item)

    write_drug(drug_list)

    cart_list[ind]['amount'] -= amount
    if cart_list[ind]['amount'] <= 0 :
        cart_list.pop(ind)

    write_cart(cart_list)

def clear_cart() :
    cart_list = read_cart()
    drug_list = read_drug()

    for i in range(len(cart_list)) :
        removed_item = cart_list[i].copy()

        for i in range(len(drug_list)) :
            if drug_list[i]['name'] == removed_item['name'] :
                drug_list[i]['amount'] += removed_item['amount']
                removed_item = ''
                break

        if removed_item != '' :
            drug_list.append(removed_item)
    
    write_cart([])
    write_drug(drug_list)

def cart() :
    while True :

        show_cart()
        inp = get_input()
        if inp == 0 :
            return 
        elif inp == 1 :
            os.system('cls')
            print('========== ADD TO CART ==========\n')
            show_drug_list_info()
            print('\n================================\n')
            add_to_cart()
        elif inp == 2 :
            remove_from_cart()
        elif inp == 3 :
            clear_cart()
