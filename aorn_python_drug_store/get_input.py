def get_input() :
    inp = input('ENTER YOUR INPUT : ')
    if inp.isnumeric() :
        return int(inp)
    else :
        return -1