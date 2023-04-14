from bs4 import BeautifulSoup, SoupStrainer
import requests
import sys
import re

base = "https://en.wikipedia.org"
url = "https://en.wikipedia.org/wiki/List_of_companies_based_in_London"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

hrefs = []
for tag in soup.find('h3').findNextSiblings():
    if tag.name == "h3":
        continue
    [hrefs.append(subtag["href"]) for subtag in tag.find_all("a")]

links = []
web_addr_regex = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
links = []
for href in hrefs:
    subresponse = requests.get(base + href)
    subsoup = BeautifulSoup(subresponse.text, 'html.parser')
    for tr in subsoup.find_all("tr"):
        if not tr.find("th") == None: 
            if not len(tr.find("th").contents) == 0:
                if tr.find("th").contents[0] == "Website":
                    if len(tr.find_all('a', {'href': re.compile(web_addr_regex)})) > 0:
                        links.append(tr.find_all('a', {'href': re.compile(web_addr_regex)})[0]["href"])

# open file in write mode
with open(r'links.txt', 'w') as fp:
    for item in links:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')