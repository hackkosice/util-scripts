#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

quote_page = 'https://a-z-animals.com/animals/'
page = requests.get(quote_page)

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find('div', attrs={'class': 'content'})
animals = content.find_all('b')

with open('animals.txt', 'w') as f:
    for animal in animals:
        f.write(animal.string.lower() + '\n')
