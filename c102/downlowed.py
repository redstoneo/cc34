import os
import shutil
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/Gerber/Downloads"
to_dir="C:/Users/Gerber/Desktop/aname"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)


event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

while True:
    print("runing")
    time.sleep(2)