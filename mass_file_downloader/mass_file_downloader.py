
import sys
import os
import requests
import re
from time import time
import platform

from html_scraper import parse


class image:

    def __init__(self, url, type, name):
        self.url = url
        self.type = type
        self.name = name
        self.fin = False


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
#need to clean up
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



#needs to make lis of objects
def make_ims(urls):

    imgs = []

    #regex for type
    type = "(\.[a-z]+)\Z"

    #regex for name (on chan) end chars trimmed
    name = "(/[0-9]{0,20}\.)"

    n = 0
    for url in urls:
        u = "http://" + url
        t = re.search(type, url).group(0)
        n = re.search(name, url).group(0)[1:-1]
        im = image(u, t, n)
        imgs.append(im)

    return imgs


#downloads files for windows
def win_mass_down(path, ims):

    i = 0
    for im in ims:
        #checks obj fin and if file with same name done 
        #need to add check for im.fin
        if(os.path.isfile(path + im.name + im.type) == False): #im.fin == False or 

            f = requests.get(im.url)
            open(path + im.name + im.type, 'wb').write(f.content)
            im.fin = True
            print(im.name + " completed")
            i = i + 1
        else:
            print("a file named " + im.name + " already exists")

            #add if file im.fin is false check and add a rename?

    print(str(i) + " files downloaded")



#function to find pattern for website
def pick_pattern(url):

    if "4chan.org" or "4channel.org" in url:
        #chan pattern
        return "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"
    elif "imgur" in url:
        #add more patterns here
        return "(?!\/)([\/.|\w|\s|-])*\.(?:jpg|gif|png|webm|jpeg)"
    else:
        #very general guess pattern
        return "(src=\"https:.{1,120}\.[a-z]{3,4})"


def main():

    #for line inputs
    url = sys.argv[1]
    path = sys.argv[2]

    pattern = pick_pattern(url)
    create_folder(path)

    #returns list of strings after parsing html specific to pattern
    urls = parse(pattern, url)

    #splice the regex as list
    urls = splice(urls)

    ims = make_ims(urls)

    if platform.system() == "Windows":
        #do win down
        win_mass_down(path, ims)
    else:
        #do regular down
        mass_down(path, ims)



def gui_main(path, url):

    pattern = pick_pattern(url)
    create_folder(path)

    #needed for path fix
    path = path + "/"

    #gets usable list of urls
    urls = parse(pattern, url)
    urls = splice(urls)
    ims = make_ims(urls)

    if platform.system() == "Windows":
        #do win down
        win_mass_down(path, ims)
    else:
        #do regular down
        mass_down(path, ims)


#main()
#gui_main(path, url)


#TODO LIST
'''
add booru sites
add imgur && more
need to clean up code in download functions

'''