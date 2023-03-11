import bs4
import requests


# See https://toscrape.com/
def print_value(label, value):
    print(f'{label}:\n{"=" * 30}\n{value}')


# s15-121 : Python Web Scraping - Book Examples Part One
# GOAL: get title of every boot with a 2-star rating
# http://books.toscrape.com/catalogue/page-2.html
# http://books.toscrape.com/catalogue/page-3.html

def s15_121():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

    page_num = 12
    print(base_url.format(page_num))

    # Look for class: product_pod
    res = requests.get(base_url.format(1))
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    products = soup.select('.product_pod')

    print_value('products count', len(products))
    for i,p in enumerate(products):
        print_value(f'product-{i}', p)


if __name__ == '__main__':
    s15_121()
