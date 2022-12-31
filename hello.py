x = (input("Enter a phrase"))
def count_wd(phrase):
    count = 0
    for w in phrase:
        if w==" ":
            count+=1
    count+=1
    print(count)
y = count_wd(x)
