def write_menu_file (menu_list) :
    f = open('menu\menu.txt','w')
    str_to_write = []
    if len(menu_list) != 0 :
        for i in range(len(menu_list)) :
            str_to_write.append(menu_list[i][0] + ' ' + str(menu_list[i][1]) + ' ' + str(menu_list[i][2]))
        str_to_write = ','.join(str_to_write)
        f.write(str_to_write)
    else :
        f.write('')
    f.close()