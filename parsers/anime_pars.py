import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from random import randint

# КАЧЕСТВО ХУЙНЯ, НО РАБОТАЕТ ЗАЕБОК ###
def get_anime():
    ua = UserAgent()
    page = randint(1, 3)
    url = f'https://www.wallpaperflare.com/search?wallpaper=Anime+Girls&page={page}'
    headers = {
        'accept': '*/*',
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.find('ul', class_='gallery').find_all('li')
    r = randint(1, 80)
    item_2 = items[r]
    item = item_2.find('img')

    return item['data-src']

