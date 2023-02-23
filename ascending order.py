def acceding(num):
    for i in range(1,len(num)):
        if num[i]<num[i-1]:
            return False
    return True
num = [1,2,3,1]
print(acceding(num))what is t