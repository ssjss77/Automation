from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import os.path

import json
import time


class MyHandler( FileSystemEventHandler) :
    i=1
    def on_modified(self, event):
        extensions = {'img' : ['.jpg', '.jpeg', '.png'], 'printed' : ['.pdf'], 'text' : ['.doc', '.docx', '.pages','.txt' ],
                      'spreadsheets' : ['.csv', '.numbers', '.xlsx', '.xls']
                      }

        for filename in os.listdir(folder_to_track):
            extension = os.path.splitext( filename )[1]
            src = folder_to_track +"/" + filename

            if (extension in extensions['img']):
                new_destination_img = folder_destinations[0] + "/" + filename
                os.rename( src, new_destination_img )

            elif (extension in extensions['printed']):
                new_destination_pdf = folder_destinations[1] + "/" + filename
                os.rename( src, new_destination_pdf )

            elif (extension in extensions['spreadsheets']) :
                new_destination_xl = folder_destinations[2] + "/" + filename
                os.rename(src, new_destination_xl)

            elif (extension in extensions['text']) :
                new_destination_txt = folder_destinations[3] + "/" + filename
                os.rename(src, new_destination_txt)


            else :
                pass


folder_to_track = '/Users/aisaidi/Downloads'
folder_destinations = ['/Users/aisaidi/Downloads/Images','/Users/aisaidi/Downloads/pdf', '/Users/aisaidi/Downloads/Tableaux','/Users/aisaidi/Downloads/Text']

event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()