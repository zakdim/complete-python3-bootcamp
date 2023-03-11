import bs4
import requests


def print_value(label, value):
    print(f'{label}:\n{"=" * 30}\n{value}')


def s15_118():
    url: str = 'https://example.com/'

    result = requests.get(url)
    # print(type(result))
    # print(f'result.text:\n{"="*30}\n{result.text}')

    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    print_value('soup', soup)

    title = soup.select('title')
    print_value('title', title)

    paragraphs = soup.select('p')
    print_value('paragraphs', paragraphs)

    h1 = soup.select('h1')
    print_value('h1', h1)

    # Grab text only
    title = soup.select('title')[0].getText()
    print_value('title', title)

    paragraphs = soup.select('p')
    print_value('paragraphs', paragraphs)


# s15-119: Grabbing a class
def s15_119():
    res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # print_value('soup', soup)

    # search for .vector-toc-text
    toc_div = soup.select('div.vector-toc-text')
    # print_value('toc_text', toc_div)

    for div in toc_div:
        toc_num_span = div.select('span.vector-toc-numb')
        toc_num = ''
        toc_text = ''
        if len(toc_num_span) > 0:
            toc_num = toc_num_span[0].text

        if len(div) >= 3:
            toc_text = div.contents[2]
        elif len(div) >=1:
            toc_text = div.contents[0]

        print(f'{toc_num}{" " if bool(toc_num) else ""}{toc_text}')


def s15_120():
    res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # print_value('soup', soup)

    images = soup.select('.thumbimage')
    # for img in images:
    #     print(img)

    computer = images[1];
    # print(computer)
    # type(computer)
    print(computer['src'])
    image_link = requests.get(f'https:{computer["src"]}')
    print(image_link.content)

    f = open('my_computer_image.jpg','wb')
    f.write(image_link.content)
    f.close()


if __name__ == '__main__':
    # s15_118()
    # s15_119()
    s15_120()
