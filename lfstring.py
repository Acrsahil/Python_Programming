rn = int(input("Enter the range of string you want to enter: "))
lst = []
for s in range(0,rn):
    t = str(input("Enter a String: "))
    lst.append(t)
print(lst)
for str in lst:
    print(str)