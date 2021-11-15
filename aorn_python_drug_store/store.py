import os
from get_input import get_input
from mange_file import read_drug
from mange_file import write_drug
from mange_file import read_cart
from mange_file import write_cart

def show_store() :
    os.system('cls')
    print('THIS IS MAIN STORE')
    show_drug_list_info()
    print('[1] SEARCH DRUG')
    print('[2] ADD DRUG TO CART')
    print('[3] ADD NEW DRUG TO LIST')
    print('[0] BACK')

def show_drug_list_info() :
    drug_list = read_drug()
    for i in range(len(drug_list)) :
        print( i , get_drug_info(drug_list[i]) )

def get_drug_info(x) :
    return 'NAME : ' + x['name'] + ' , PRICE ' + str(x['price']) + ' , AMOUNT : ' + str(x['amount'])

def show_search_resault() :
    os.system('cls')
    inp = input('ENTER NAME TO SEARCH : ')
    print('SEARCH RESAULT')

    drug_list = read_drug()

    for i in range(len(drug_list)) :
        if inp in drug_list[i]['name'] :
            print( i , get_drug_info(drug_list[i]) )

    print('[1] ADD TO CART')
    print('[0] BACK')

    inp = get_input()
    if inp == 1 :
        add_to_cart()
    
def add_to_cart() :
    drug_list = read_drug()
    cart_list = read_cart()

    ind = input('ENTER INDEX TO ADD : ')
    while not( ind.isnumeric() and 0 <= int(ind) and int(ind) < len(drug_list) ) :
         ind = input('ENTER POSITIVE INTEGER : ')
    ind = int(ind)

    amount = input('ENTER AMOUNT : ')
    # print(drug_list[ind])
    while not( amount.isnumeric() and int(amount) <= drug_list[ind]['amount'] ) :
         amount = input('ENTER POSITIVE INTEGER : ')
    amount = int(amount)

    new_to_cart = drug_list[ind].copy()
    new_to_cart['amount'] = amount
    for i in range(len(cart_list)) :
        if cart_list[i]['name'] == new_to_cart['name'] :
            cart_list[i]['amount'] += amount
            new_to_cart = ''
            break

    if new_to_cart != '' :
        cart_list.append(new_to_cart)

    write_cart(cart_list)

    drug_list[ind]['amount'] -= amount

    if drug_list[ind]['amount'] == 0 :
        drug_list.pop(ind)
    
    write_drug(drug_list)

def add_new_drug() :
    os.system('cls')
    name = input('ENTER NAME : ')

    price = input('ENTER PRICE : ')
    while not( price.isnumeric() and int(price) > 0 ) :
        price = input('ENTER POSITIVE INTEGER : ')

    amount = input('ENTER AMOUNT : ')
    while not( amount.isnumeric() and int(amount) > 0 ) :
        amount = input('ENTER POSITIVE INTEGER : ')

    drug_list = read_drug()
    new_drug = { 'name' : name , 'price' : price , 'amount' : amount }
    drug_list.append(new_drug)
    write_drug(drug_list)
    

def store() :
    while True :

        show_store()
        
        inp = get_input()
        if inp == 0 :
            return 
        elif inp == 1 :
            show_search_resault()
        elif inp == 2 :
            add_to_cart()
        elif inp == 3 :
            add_new_drug()



