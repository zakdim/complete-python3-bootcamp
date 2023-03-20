import csv
import requests
from pathlib import Path
import PyPDF2
import re


def extract_url(csv_data):
    index = 0
    url = ''
    for line in list(csv_data)[0:]:
        url += line[index]
        index += 1

    return url


def download_pdf(url):
    output_file = Path('./exercise-files/pdf-response.pdf')
    res = requests.get(url)
    output_file.write_bytes(res.content)


def find_phone(file_name):
    f = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)
    # print(len(pdf_reader.pages))
    phone_pattern = re.compile(r'\d{3}[ -.]\d{3}[ -.]\d{4}')
    phone = None

    for num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[num]
        # print(f'PAGE-{num}: {page.extract_text()}')
        phone = re.search(phone_pattern, page.extract_text())
        # print(f'PAGE-{num}, phone={phone}')
        if phone is not None:
            phone = phone.group()
            break

    return phone


def s17_132():
    data = open('exercise-files/find_the_link.csv', encoding='utf-8')
    csv_data = csv.reader(data)

    url = extract_url(csv_data)
    print(f'EXTRACTED URL: {url}')

    # download_pdf(url)
    phone = find_phone('./exercise-files/Find_the_Phone_Number.pdf')
    if phone is not None:
        print(f'FOUND PHONE: {phone}')

    data.close()


if __name__ == '__main__':
    s17_132()
