import bs4
import requests

url: str = 'https://example.com/'

result = requests.get(url)
# print(type(result))
# print(f'result.text:\n{"="*30}\n{result.text}')

soup = bs4.BeautifulSoup(result.text, 'html.parser')
# print(f'soup:\n{"="*30}\n{soup}')

title = soup.select('title')
print(f'title:\n{"="*30}\n{title}')

paragraphs = soup.select('p')
print(f'paragraphs:\n{"="*30}\n{paragraphs}')

h1 = soup.select('h1')
print(f'h1:\n{"="*30}\n{h1}')

# Grab text only
title = soup.select('title')[0].getText()
print(f'title:\n{"="*30}\n{title}')

paragraphs = soup.select('p')
print(f'paragraphs:\n{"="*30}\n{paragraphs[0].getText()}')