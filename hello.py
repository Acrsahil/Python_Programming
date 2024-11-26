lst = [-2, 5, -2, -8, -2, -5, -7]

i = 0

sum = 0
ans = -2342424244
while i < len(lst):
    sum += lst[i]
    ans = max(sum, ans)

    if sum < 0:
        sum = 0
    i += 1

print(ans)
