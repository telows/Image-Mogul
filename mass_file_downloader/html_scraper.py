
import requests
import re

#use str url to get page html as str
def page_text(url):
    p = requests.get(url)
    return p.text

#parses through pattern returns list of strings


#gets 2 of every url
def parse(pattern, url):
    return re.findall(pattern, page_text(url))




#print(parse("(href=\"//is2.4chan.org/.{1,22}\")" , "http://boards.4channel.org/c/thread/3510179"))
