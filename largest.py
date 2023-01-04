len = int(input("Enter the list of the number you want to check: "))
lst = []
for i in range(0,len):
    num = int(input('Enter the number: '))
    lst.append(num)

largest = lst[0] # first index of the list
for n in lst: # input:2,14,4,23
    if n > largest: # 2>2,14>2,4>14,23>14
        largest = n # largest = 2,14,23
print(largest,"is the largest number in list")

