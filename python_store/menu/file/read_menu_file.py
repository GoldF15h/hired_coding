def read_menu_file () :
    PATH = 'menu\menu.txt'
    f = open(PATH,'r')
    text = f.read()
    if len(text) == 0 :
        return []
        
    menu_list = text.split(',')
    for i in range(len(menu_list)) :
        try :
            tmp = menu_list[i].split()
            menu_list[i] = [tmp[0],int(tmp[1]),int(tmp[2])]
        except :
            return []
    f.close()
    return menu_list