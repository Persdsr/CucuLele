import random

import requests


# НОРМ, НО РАБОТАЕТ ХУЕВО
def get_anime():

    token = '175e41cf175e41cf175e41cf94144fc1de1175e175e41cf742b1c35e95cf87e30174d8c'
    version = 5.131
    domain = 'trendiy'

    offset = random.randint(1, 100)

    r = requests.get('https://api.vk.com/method/wall.get',
                     params={
                         'access_token': token,
                         'v': version,
                         'domain': domain,
                         'offset': 1
                     })

    data = r.json()['response']['items']
    items_len = len(data)
    all_items = []
    b = random.randint(0, 8)
    for d in data:
        try:
            for i in d['attachments'][b]['photo']['sizes']:
                if i['type'] == 'z':
                    all_items.append(i['url'])
        except:
            continue
    a = random.randint(0, len(all_items))
    return all_items[a]
