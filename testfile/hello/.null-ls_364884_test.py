import os

import shutil as sh

source = "/home/window/codehub/Python_Programming/testfile/"
dest = "/home/window/codehub/Python_Programming/testfile/hello/"


def fileprint(source):
    with os.scandir(source) as files:
        for file in files:
            ext = os.path.splitext(file.name)
            print(f"Move file {ext}")
            sh.move(os.path.join(source, file), dest)


fileprint(source)
