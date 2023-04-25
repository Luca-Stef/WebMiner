from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://intropic.io/")
soup = BeautifulSoup(response.text, 'lxml')

ite = re.finditer("mailto", response.text)
indices = [m.start(0) for m in ite]