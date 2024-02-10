num = [1, 2, 22, 4, 5]
for i in range(1, len(num)):
    if num[i] < num[i - 1]:
        print(False)

    else:
        print(True)
