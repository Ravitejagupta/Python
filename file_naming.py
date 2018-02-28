def fileNaming(names):
    list = []
    i = 0
    for name in names:
        if name not in list:
            list.append(name)
            
        else:
            i = i+1
            
            name = name + "({})".format(str(i))
            list.append(name)
            i=1
            
    return list
