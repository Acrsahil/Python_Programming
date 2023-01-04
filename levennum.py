len = int(input("Enter a range: "))
lst = []
for i in range(0,len):
    num = int(input("Enter a number: "))
    lst.append(num)
even= []
for n in lst:
    if n%2 == 1:
        continue
    even.append(n)
print(even)







