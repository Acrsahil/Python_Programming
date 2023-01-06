def listc(lst):
    unique = set()
    for num in lst:
        if num in unique:
            return True
        unique.add(num)
    return False
lst = [2, 4, 5, 6, 8, 7,"sahil",]

print(listc(lst))
