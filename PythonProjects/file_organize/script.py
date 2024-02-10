def readfile(file):
    for line in file:
        line = line.strip()
        print(line)


try:
    file = open("demo.txt", "r")
    readfile(file)
    file.close()
    print("Before the file changes!")

    file = open("demo.txt", "a")
    file.write("One last line!")
    file.close()

    file = open("demo.txt", "r")
    readfile(file)
    file.close()
    print("After the file changes!")

except FileNotFoundError:
    print("File is not found in the given directory")
