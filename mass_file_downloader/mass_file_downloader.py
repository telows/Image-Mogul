
import sys
import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

from html_scraper import parse


#downloader
def time():
    start = time()

    for x in urls:
        url_response(x)
        print("downloaded in {time() - start} seconds")


#single file download
def download(url, file):

    file = requests.get(url)
    open("path", 'wb').write(file.content)


#creates folder at path
def create_folder(path):

    access_rights = 0o755
    if(os.path.exists(path) == False):
        os.makedirs(path, access_rights)


def splice(lis):

    n = 0
    for i in lis:
        #[8:len(str) - 1]
        i = i[8: len(i)-1]
        lis[n] = i
        n = n + 1

    return lis

#need to check redundency in files
def mass_down(path, urls):

    i = 0
    for url in urls:

        fname = url[16:-4]
        name = path + fname

        if(os.path.isfile(name) == False):
            f = requests.get( "https://" + url)
            open(path + url[16: len(url) - 4], 'wb').write(f.content)
            i = i + 1
            print(fname + " completed")
        else:
            print("a file named " + url[16: len(url) -4] + " already exists")

            #d = input("would you like to download the file anyways y/n?")

            #if(d == 'y'):
            #    f = requests.get( "https://" + url)
            #    open(path + url[16: len(url) - 4] + '(1)', 'wb').write(f.content)
            #    i = i + 1
            #    print(fname + " completed")

            #return a list of undownloaded files?

    print(str(i) + " files downloaded")


def main():

    pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"

    #test stuff
    url = "http://boards.4channel.org/c/thread/3510179"
    path = "/home/ryan/Pictures/test/"

    #for line inputs
    #url = sys.argv[1]
    #path = sys.argv[2]

    create_folder(path)


    #returns list of strings after parsing html
    urls = parse(pattern, url)
    #print(urls)

    #splice the regex as list
    urls = splice(urls)

    #print(urls)

    #download spliced regex retrival
    #save to folder
    mass_down(path, urls) #need fix



main()
