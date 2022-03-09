import time

import requests
from source import utils, conf

utils.check_os()
utils.check_setup()

configuration = conf.load_conf()


def invite():
    print("Generating new invite!")
    resp = requests.post(
        'https://discordapp.com/api/channels/{}/invites'.format(configuration.discord_welcome_room),
        headers={'Authorization': 'Bot {}'.format(configuration.discord_token)},
        json={'max_uses': 1, 'unique': True, 'max_age': 300}
    )
    i = resp.json()
    if i.get('code'):
        print("Generated new invite!")
    else:
        print(f"Sleeping for {i.get('retry_after')}")
        time.sleep(i.get("retry_after")/2)
        return invite()

    return i["code"]
