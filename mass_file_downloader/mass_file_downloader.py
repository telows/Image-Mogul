
import sys
import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

#multifile download
def urlresponse(url):
    path = url
    url = url

    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)

#4chanregex = (href="//is2.4chan.org/.{1,22}")


#downloader
start = time()

for x in urls:
    url_response(x)
print("downloaded in {time() - start} seconds")


#single file download
def download(url, file):
    #need input for url

    file = requests.get(url)
    open("path", 'wb').write(file.content)


create_folder(path):
    #path = "input path as string"
    access_rights = 0o755
    os.mkdir(path, access_rights)




def main():

    #open/make folder

    #get thread url (from command line)?
url = sys.argv[1]
    #put thread html in .txt file

    #parse html w/ regex

    #download spliced regex retrival
    #save to folder


main()