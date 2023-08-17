import requests
from bs4 import BeautifulSoup


def load(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        with open(f'media/good_morning/{i}.jpg', 'wb') as f:
            f.write(response.content)
        return (True, response.status_code)
    else:
        return (False, response.status_code)


for i in range(8073, 8174):
    print(f'Trying load image {i}')
    f = (False,)
    while not f[0]:
        f = load(f'https://photovords.ru/pics_max/photowords_ru_{i}.jpg')
        if f[0]:
            print(f'    Image {i} loaded')
        else:
            print(f'I   mage {i} not loaded with code {f[1]}')
