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

    # page_num = 12
    # print(base_url.format(page_num))
    #
    # # Look for class: product_pod
    # res = requests.get(base_url.format(1))
    # soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # products = soup.select('.product_pod')
    #
    # for i,p in enumerate(products):
    #     print_value(f'product-{i}', p)
    # example = products[0]
    # print_value('product-00', example)
    #
    # # Method-1: quick and dirty
    # print_value('isStarRatingTwo', 'star-rating Two' in str(example))
    #
    # # Method-2: select using class
    # is_two_start_rating = bool(example.select('.star-rating.Two'))
    # print_value('is_two_star_rating', is_two_start_rating)
    #
    # # Select title
    # title = example.select('a')[1]['title']
    # print_value('title', title)

    two_start_titles = []
    for n in range(1, 51):
        scrape_url = base_url.format(n)
        res = requests.get(scrape_url)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        books = soup.select('.product_pod')

        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                title = book.select('a')[1]['title']
                two_start_titles.append(title)

    for i,b in enumerate(two_start_titles):
        print(f'[{i+1:03d}]: {b}')


if __name__ == '__main__':
    s15_121()
