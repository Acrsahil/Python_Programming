def listc(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    if unique in lst:
        print(True)
    else:
        print(False)
    lst = [2, 4, 5, 6, 8, 7, 7]
    x = listc(lst)
