def read_member() :
    f = open('member.txt','r')
    txt = f.read()
    member_list = txt.split('\n')
    for i in range(len(member_list)) :
        name , phone = member_list[i].split('`')
        member_list[i] = {'name' : name , 'phone_num' : phone,}
    f.close()
    return member_list

def write_member(member_list) :
    f = open('member.txt','w')
    for i in range(len(member_list)) :
        member_list[i] = str(member_list[i]['name']) + '`' + str(member_list[i]['phone_num'])
    txt_to_write = '\n'.join(member_list)
    f.write(txt_to_write)
    f.close()

def read_menu(file) :
    f = open(file,'r')
    txt = f.read()
    menu_list = txt.split('\n')
    for i in range(len(menu_list)) :
        tmp_menu = menu_list[i].split(' , ')
        # print(tmp_menu)
        menu_list[i] = (tmp_menu[0] ,tmp_menu[1])
    f.close()
    return menu_list

def write_recipt(new_recipt) :
    f = open('Recipt.txt','a')
    f.writelines('\n'+new_recipt)
    f.close()

if __name__ == '__main__' :
    # l = read_member()
    # l.append({'name':'testWrite','phone_num':999})
    # write_member(l)
    l = read_menu('Coffee.txt')
    l = read_menu('Dessert.txt')
    l = read_menu('Juice.txt')
    l = read_menu('Tea.txt')
    # print(l)      
    # print(type(l[0]))