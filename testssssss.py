import requests


s = 0
for i in range(811, 912):
    url = f'https://dobrogoutra.ru/noname/imgbig/dobrogoutra_ru_10{i}.jpg'

    response = requests.get(url)

    if response.status_code == 200:
        with open(f'media/good_evening/{s}.jpg', 'wb') as f:
            f.write(response.content)
        print(f'Image {s}.jpg({i}) loaded')
        s += 1
    else:
        print(f'Image {i} not loaded - {response.status_code}\n     url - {url}')
