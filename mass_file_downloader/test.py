
from mass_file_downloader import create_folder
import os


#teststuff
pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"
url = "http://boards.4channel.org/c/thread/3510179"
path = "/home/ryan/Pictures/test/"


if(os.path.exists(path) == False):
    create_folder(path)
    print("1")
