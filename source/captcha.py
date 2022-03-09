import json

from source import conf
from source import utils
import requests
import urllib.parse

utils.check_os()
utils.check_setup()

configuration = conf.load_conf()


def handle(code, ip=None):
    if configuration.captcha == "recaptcha":
        payload = {
            'secret': configuration.captcha_private,
            'response': code,
        }
        if not ip is None:
            payload['remoteip'] = ip
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=json.dumps(payload))
        result = response.json()
        return result.get('success', False)
    elif configuration.captcha == "hcaptcha":
        payload = {
            'secret': urllib.parse.quote(configuration.captcha_private),
            'response': urllib.parse.quote(code),
        }
        url = f"https://hcaptcha.com/siteverify?secret={payload['secret']}&response={payload['response']}"
        response = requests.post(url)
        result = response.json()
        return result.get('success', False)