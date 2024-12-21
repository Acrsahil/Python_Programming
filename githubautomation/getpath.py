path = ""


def getpath():
    path = input("Path: ")
    with open(
        "/home/window/codehub/Python_Programming/githubautomation/path.txt", "w"
    ) as file:
        file.write(path)
    print("file is written sucessfully")


def prints():
    return path


if __name__ == "__main__":
    getpath()
else:
    prints()
