def cprime(num):
    for i in range(2, num):
        if (num%i) == 0:
            return False
    return True
def all_prime(num):
    for n in range(2,num+1):
        if cprime(n):
            print(n)
num = int(input("Enter a numbers: "))
x = (all_prime(num))
