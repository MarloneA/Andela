def data_type(arg):
    
    if type(arg) == int:
        if arg == 100:
            return 'equal to 100'
        elif arg < 100:
            return 'less than 100'
        else:
            return 'more than 100'
    
    if type(arg) == str:
        return len(arg)
    
    if type(arg) == bool:
        return arg
    
    if type(arg) == list:
        if len(arg) < 3:
            return None
        else:
            return arg[2]
    if arg is None:
        return 'no value'