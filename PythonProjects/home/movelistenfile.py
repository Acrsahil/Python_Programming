import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

Downloads = "/home/window/Downloads/"
Viber = "/home/window/Documents/ViberDownloads/"
Music = "/home/window/Music/"
Pictures = "/home/window/Pictures/"
Video = "/home/window/Videos/"
Mountcare = "/home/window/Documents/Mountcare/"
Pdf = "/home/window/Documents/Pdf/"
Document = "/home/window/Documents/"


class MyHandler(FileSystemEventHandler):
    def __init__(self, folder_to_track, default_destination):
        self.folder_to_track = folder_to_track
        self.default_destination = default_destination

    def determine_destination(self, file_name):
        video_extensions = [
            ".mp4",
            ".mkv",
            ".avi",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".m4v",
            ".3gp",
            ".mpg",
            ".mpeg",
        ]
        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        music_extensions = [".mp3", ".wav", ".flac", ".aac"]
        document_extensions = [".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"]
        ext = os.path.splitext(file_name)[-1].lower()

        if ext in image_extensions:
            return Pictures
        elif ext in video_extensions:
            return Video
        elif ext == ".pdf":
            return Pdf
        elif ext in document_extensions:
            return Document
        elif ext in music_extensions:
            return Music
        else:
            return self.default_destination

    def on_created(self, event):
        if event.is_directory:
            return  # Ignore directory creation events

        filename = os.path.basename(event.src_path)
        src = os.path.join(self.folder_to_track, filename)
        destination = self.determine_destination(filename)
        new_destination = os.path.join(destination, filename)

        # Check if it's a file before trying to move
        if os.path.isfile(src):
            os.rename(src, new_destination)
            print(f"Moved: {filename} to {destination}")


if __name__ == "__main__":
    folder_to_track = "/home/window/Downloads/"
    default_destination = "/home/window/Downloads/newfolder/"

    event_handler = MyHandler(folder_to_track, default_destination)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
