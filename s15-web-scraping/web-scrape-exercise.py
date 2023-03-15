import bs4
import requests
from com.github.zakdim.utils import utils


# See  http://quotes.toscrape.com/
# s15-123 : Python Web Scraping - Exercise

def get_authors(page, soup):
    authors = set()
    for author in soup.select('.author'):
        authors.add(author.text)

    # utils.print_value(f'Authors (page-{page:03d})', sorted(set(authors)))
    return authors


def get_quotes(page, soup):
    quotes = []
    for quote in soup.select('.quote>.text'):
        quotes.append(quote.text)

    return quotes


def get_top_ten_tags(page, soup):
    tags = []
    for tt in soup.select('.tags-box .tag'):
        tags.append(tt.text)

    return tags;


def process_first_page(page, soup):
    # Task-01: get names of all the authors
    authors = get_authors(page, soup)
    utils.print_value(f'Authors (page-{page:03d})', sorted(authors))

    # Task-02: create a list of all the quotes
    quotes = get_quotes(page, soup)
    utils.print_value(f'Quotes (page-{page:03d})')
    for q in quotes:
        print(q)

    # Task-03: top ten tags
    top_tags = get_top_ten_tags(page, soup)
    utils.print_value(f'Top ten tags (page-{page:03d})', top_tags)

    return authors


def s15_123():
    home_url = 'http://quotes.toscrape.com'
    page_url_path = '/page/{}/'
    page_threshold = 100
    first_page = True
    unique_authors = set()

    for i in utils.int_stream():
        scrape_url = home_url
        page = i + 1
        if page <= 1:
            first_page = True
        else:
            first_page = False
            scrape_url = home_url + page_url_path.format(page)

        utils.print_value('Scraping URL', scrape_url)

        res = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if 'No quotes found!' in soup.text or page >= page_threshold:
            print(f'END OF QUOTES on page {page}')
            break

        if first_page:
            unique_authors.update(process_first_page(page, soup))
        else:
            unique_authors.update(get_authors(page, soup))

    print('Unique authors:')
    for i, author in enumerate(sorted(unique_authors)):
        print(f'{i + 1:03d}: {author}')


if __name__ == '__main__':
    s15_123()
