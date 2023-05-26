from bs4 import BeautifulSoup
import requests
import random
import sys


def parse():
    URL = 'https://uprostim.com/204-kartinki-motiviruyushhie-na-uspeh/'

    try:
        page = requests.get(URL)
    except Exception as _ex:
        print(_ex)
        sys.exit(0)

    print(page.status_code)
    for key, value in page.request.headers.items():
        print(key + ": " + value)

    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.findAll('a')
    images = []
    for data in items:
        if data.find('img'):
            images.append(data.get('href'))
    print(images)
    return images


motivation_img = parse()


def random_img():
    index = random.randrange(len(motivation_img))
    return motivation_img[index]
