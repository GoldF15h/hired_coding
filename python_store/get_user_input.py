def get_user_input () :
    print('TYPE YOUR INPUT : ',end='')
    inp = input()
    if len(inp) == 1 :
        return inp
    else :
        return ''