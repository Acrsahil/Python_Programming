def rem_dup(lst):
    rem = []
    for i in lst:
        if i not in rem:
            rem.append(i)
    return rem
to_rem = ["ram",1,2,1,2,5,5,6,7,6,5]
print(rem_dup(to_rem))
