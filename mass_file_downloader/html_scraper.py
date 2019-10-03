
import requests
import re

#use url to get page html as str
def page_text(url):
    p = requests.get(url)
    return p.text


#parses through pattern returns list of strings
def parse(pattern, url):
    return re.findall(pattern, page_text(url))
