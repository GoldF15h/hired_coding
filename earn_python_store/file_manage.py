def read_member() :
    f = open('member.txt','r')
    txt = f.read()
    member_list = txt.split('\n')
    for i in range(len(member_list)) :
        name , phone = member_list[i].split('`')
        member_list[i] = {'name' : name , 'phone_num' : phone,}
    return member_list

def write_member(member_list) :
    f = open('member.txt','w')
    for i in range(len(member_list)) :
        member_list[i] = str(member_list[i]['name']) + '`' + str(member_list[i]['phone_num'])
    txt_to_write = '\n'.join(member_list)
    f.write(txt_to_write)

if __name__ == '__main__' :
    l = read_member()
    l.append({'name':'testWrite','phone_num':999})
    write_member(l)
    # print(l)
    # print(l[0]['phone_num'])