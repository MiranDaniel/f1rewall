import time

import requests
from blessed import Terminal

from source import utils, conf

utils.check_os()
utils.check_setup()


term = Terminal()


configuration = conf.load_conf()


def invite(size=1):
    print("::InvitePool::  "+term.reverse(term.green4("Generating new invite!")))
    resp = requests.post(
        'https://discordapp.com/api/channels/{}/invites'.format(configuration.discord_welcome_room),
        headers={'Authorization': 'Bot {}'.format(configuration.discord_token)},
        json={'max_uses': size, 'unique': True, 'max_age': 300}
    )
    i = resp.json()
    if i.get('code'):
        print("::InvitePool::  "+term.reverse(term.green(f"Generated new invite! {i['code']}")))
    else:
        print("::InvitePool::  "+term.reverse(term.red(f"Sleeping for {i.get('retry_after')}")))
        time.sleep(i.get("retry_after")/2)
        return None

    return i["code"]
