import os
import shutil as sh


Downloads = "/home/window/Downloads/"
Viber = "/home/window/Documents/ViberDownloads/"
Music = "/home/window/Music/"
Pictures = "/home/window/Pictures/"
Video = "/home/window/Videos/"
Mountcare = "/home/window/Documents/Mountcare/"
Pdf = "/home/window/Documents/Pdf/"


def MoveDocument(source):
    with os.scandir(source) as files:
        for file in files:
            ext = os.path.splitext(file.name)
            print(ext)

            if ext[-1] == ".m4a":
                print(f"Moved file {ext}")
                sh.move(os.path.join(source, file), Music)

            elif ext[-1] == ".jpg" or ext[-1] == ".png":
                print(f"Moved file {ext}")
                sh.move(os.path.join(source, file), Pictures)

            elif ext[-1] == ".mp4":
                print(f"Moved file {ext}")
                sh.move(os.path.join(source, file), Video)

            elif ext[-1] == ".pdf":
                print(f"Moved file {ext}")
                # sh.move(os.path.join(source, file), Pdf)

            elif (
                ext[0] == "Mountcare" or ext[0] == "mountcare" or ext[0] == "MountCare"
            ):
                print(f"Moved file {ext}")
                # sh.move(os.path.join(source, file), Mountcare)


MoveDocument(Downloads)
