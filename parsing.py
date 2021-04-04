# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)

styles = soup.find_all('body', class_='background')
print(styles)
for style_element in styles:
    print(style_element)