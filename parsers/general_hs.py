from random import randint

import requests


def get_meme():
    token = '175e41cf175e41cf175e41cf94144fc1de1175e175e41cf742b1c35e95cf87e30174d8c'
    version = 5.131
    domain = 'general_hs'

    offset = randint(1, 100)
    r = requests.get('https://api.vk.com/method/wall.get',
            params={
                'access_token': token,
                'v': version,
                'domain': domain,
                'offset': offset
            })

    data = r.json()['response']['items']
    all_items = []
    for d in data:
        try:
            for i in d['attachments'][0]['photo']['sizes']:
                if i['type'] == 'z':
                    all_items.append({
                        'url': i['url'],
                        'text': d['text']
                    })
        except:
            continue

    a = randint(0, len(all_items))
    meme = all_items[a]
    return meme


get_meme()
