from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

headers = doc.select('.heading-25-extrabold.color-black')

for header in headers:
    print(header.contents[0].strip())

