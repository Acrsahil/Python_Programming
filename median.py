rn = int(input("Enter a range of the you want to find midein: "))
lst = []

for n in range(0, rn):
    num = int(input("Enter a number: "))

    lst.append(num)
lst.sort()

print(lst)

if rn % 2 == 0:
    mid = lst[rn // 2 - 1 : rn // 2 + 1]

    sum = 0

    for p in mid:
        sum += p

    median = sum / len(mid)

else:
    median = lst[rn // 2]

print("the median of the given list is", median)
