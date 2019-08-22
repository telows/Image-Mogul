
from mass_file_downloader import create_folder
import os
from tkinter import *


#teststuff
pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"
url = "http://boards.4channel.org/c/thread/3510179"
path = "/home/ryan/Pictures/test/"

wpath ="C:\\Users\\XPS\\Documents/test/"

if(os.path.exists(wpath) == False):
    create_folder(wpath)
    print("1")


