import requests
from fake_useragent import UserAgent
from random import randint

def get_anime():
    ua = UserAgent()

    url1 = 'https://ru.pinterest.com/resource/BaseSearchResource/get/?source_url=%2Fsearch%2Fpins%2F%3Fq%3Dsexy%2520anime%2520girls%26rs%3Dtyped&data=%7B%22options%22%3A%7B%22article%22%3A%22%22%2C%22appliedProductFilters%22%3A%22---%22%2C%22query%22%3A%22sexy%20anime%20girls%22%2C%22scope%22%3A%22pins%22%2C%22auto_correction_disabled%22%3A%22%22%2C%22top_pin_id%22%3A%22%22%2C%22filters%22%3A%22%22%7D%2C%22context%22%3A%7B%7D%7D&_=1673114855221'
    url2 = 'https://ru.pinterest.com/resource/BaseSearchResource/get/?source_url=%2Fsearch%2Fpins%2F%3Fq%3D%25D0%259A%25D1%2580%25D0%25B0%25D1%2581%25D0%25B8%25D0%25B2%25D0%25B0%25D1%258F%2520%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25BC%25D0%25B5%2520%25D0%25B4%25D0%25B5%25D0%25B2%25D1%2583%25D1%2588%25D0%25BA%25D0%25B0%26b_id%3DBNi4vvGeLxUnAAAAAAAAAACEN0RCTHvsHL8hGObzK9ifosgF5LvmvopKz6x-1thGP_DNdaheXfuFvEL7XutBNNJP7APrwyve5Y9RxdktXyvXs5B8qYlIPU4JZhIrfIut6MDIk8HwESi9qBqxXVBEjFYptgyCfTgs9PNmoEvMNecxLBingCnklGJsB9Ipcz20BlzulhCXXPHl40KTOjN2k4cuSSk4LNwu4w%26source_id%3Drlp_AMS6O7Kp&data=%7B%22options%22%3A%7B%22article%22%3A%22BNi4vvGeLxUnAAAAAAAAAACEN0RCTHvsHL8hGObzK9ifosgF5LvmvopKz6x-1thGP_DNdaheXfuFvEL7XutBNNJP7APrwyve5Y9RxdktXyvXs5B8qYlIPU4JZhIrfIut6MDIk8HwESi9qBqxXVBEjFYptgyCfTgs9PNmoEvMNecxLBingCnklGJsB9Ipcz20BlzulhCXXPHl40KTOjN2k4cuSSk4LNwu4w%22%2C%22appliedProductFilters%22%3A%22---%22%2C%22query%22%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D0%B0%D1%8F%20%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5%20%D0%B4%D0%B5%D0%B2%D1%83%D1%88%D0%BA%D0%B0%22%2C%22scope%22%3A%22pins%22%2C%22auto_correction_disabled%22%3A%22%22%2C%22top_pin_id%22%3A%22%22%2C%22filters%22%3A%22%22%7D%2C%22context%22%3A%7B%7D%7D&_=1673353756010'
    url = url2
    headers = {
        'accept': '*/*',
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers).json()

    items = response.get('resource_response').get('data').get('results')
    r = randint(0, len(items))

    anime = items[r]['images']['orig']['url']

    return anime



