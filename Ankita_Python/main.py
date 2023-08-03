#wap to add list only even number from the given range

lst = []
a = int(input("Enter the range: "))
for i in range(1,a+1):
    b = int(input("Enter the number: "))
    if b&1:
        lst.append(b)
print(lst)










