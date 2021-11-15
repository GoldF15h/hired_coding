def read_drug() :
    f = open("drug_list.txt", "r")
    txt = f.read()
    f.close()
    l = []
    if len(txt) > 0 :
        l = txt.split('\n')
        for i in range(len(l)) :
            l[i] = l[i].strip().split(' ')
            l[i] = {
                'name' : l[i][0] ,
                'price' : int(l[i][1]) ,
                'amount' : int(l[i][2])
            }
    return l

def write_drug(l) :
    f = open("drug_list.txt", "w")
    # l.append(['testWrite',132,222])
    str_to_write = []
    if len(l) > 0 :
        for i in range(len(l)) :
            str_to_write.append( l[i]['name'] + ' ' + str(l[i]['price']) + ' ' + str(l[i]['amount']) )
        str_to_write = '\n'.join(str_to_write)
        f.write(str_to_write)
    else :
        f.write('')
    f.close()

def read_cart() :
    f = open("cart_list.txt", "r")
    txt = f.read()
    f.close()
    l = []
    if len(txt) > 0 :
        l = txt.split('\n')
        for i in range(len(l)) :
            l[i] = l[i].strip().split(' ')
            l[i] = {
                'name' : l[i][0] ,
                'price' : int(l[i][1]) ,
                'amount' : int(l[i][2])
            }
    return l

def write_cart(l) :
    f = open("cart_list.txt", "w")
    # l.append(['testWrite',132,222])
    str_to_write = []
    if len(l) > 0 :
        for i in range(len(l)) :
            str_to_write.append( l[i]['name'] + ' ' + str(l[i]['price']) + ' ' + str(l[i]['amount']) )
        str_to_write = '\n'.join(str_to_write)
        f.write(str_to_write)
    else :
        f.write('')
    f.close()

