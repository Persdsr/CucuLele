import random

import requests

# КАЧЕСТВО 6.5/10, РАБОТАЕТ ХУЕВО
def get_anime():
    token = '175e41cf175e41cf175e41cf94144fc1de1175e175e41cf742b1c35e95cf87e30174d8c'
    version = 5.131
    domain = 'baakeneko'

    offset = random.randint(1, 12)
    r = requests.get('https://api.vk.com/method/wall.get',
            params={
                'access_token': token,
                'v': version,
                'domain': domain,
                'offset': offset
            })

    data = r.json()['response']['items']
    items_len = len(data)
    all_items = []
    for d in data:
        try:
            for i in d['attachments'][0]['photo']['sizes']:
                if i['type'] == 'z':
                    all_items.append(i['url'])
        except:
            continue

    a = random.randint(0, items_len)
    anime = all_items[a]
    return anime
