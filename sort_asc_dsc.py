numbers = input("Enter a numbers: ").split()
numbers = [int(x) for x in numbers]
numbers.sort()
print("Ascending order : ", numbers)
numbers.sort(reverse= True)
print("Descending order: ",numbers)


