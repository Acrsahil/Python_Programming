def cprime(num):
    for i in range(2, num):
        if (num%i) == 0:
            return False
    return True
def all_prime(num):
    prime = []
    for n in range(2,num+1):
        if cprime(n) is True:
            prime.append(n)
    return prime
num = int(input("Enter a numbers"))
print(all_prime(num))




