from bs4 import BeautifulSoup
import requests
import re

response = input("Enter the website url: ") 
soup = BeautifulSoup(response.text, 'lxml')
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

ite = re.finditer("mailto", response.text)
indices = [m.start(0) for m in ite]
emails = []

for i in indices:
    emails.append(re.findall(pattern, response.text[i:i+40])[0])

print(emails)