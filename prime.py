n = int(input("enter a number to find a prime: "))
for num in range(2,n):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num)
    