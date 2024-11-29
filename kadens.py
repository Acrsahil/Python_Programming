lst = [-1, -3, -1, 5, 8, -14]


n = len(lst)

sum = 0
maxi = -12342134234

start = -1
ansed = -1

for i in range(n):
    if sum == 0: start = i
    sum += lst[i]

    if sum > maxi:
        maxi = sum
        ansed = i

    if sum < 0:
        sum = 0

print(f"start {start} end {ansed}")
