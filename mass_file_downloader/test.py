import sys
import os
import requests
from mass_file_downloader import create_folder, splice, mass_down
from html_scraper import parse
from tkinter import *

import platform

#teststuff
#pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"
#url = "http://boards.4channel.org/c/thread/3510179"
#path = "/home/ryan/Pictures/test/"

#wpath ="C:\\Users\\XPS\\Documents/test/"
wpath = "C:\\Users\\Public\\Pictures\\test\\"


#more general regex works on gelbooru kinda **check with larger html**
#(?<!data-)
testpattern = "(src=\"https:.{1,120}\.jpg)"



def win_splice(lis):
	n = 0
	for i in lis:
		i = i[5:-12]
		lis[n] = i + ".jpg"
		n = n + 1

	return lis




def win_mass_down(path, urls):

    i = 0
    for url in urls:

        fname = str(i) 
        name = wpath + fname

        if(os.path.isfile(name) == False):

            f = requests.get(url)
            open(wpath + fname + ".jpg", 'wb').write(f.content)
            i = i + 1
            print(fname + " completed")

        else:
            print("a file named " + fname + " already exists")

    print(str(i) + " files downloaded")


#main apparatus
#create_folder(wpath)
#urls = parse(pattern, url)
#print(urls)
#urls = win_splice(urls)
#print(urls)
#win_mass_down(pattern, urls)


platform.system()

#check for 404 error on download