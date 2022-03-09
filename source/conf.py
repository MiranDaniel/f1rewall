import yaml
import os

class Configuration:
    class Default:
        captcha = "recaptcha/hcaptcha"
        captcha_public = "your captcha public key"
        captcha_private = "your captcha private key"
        discord_token = "your discord token"
        analytics = "false/true"
        discord_welcome_room = 0
        args = {
            "You can put additional settings here": "Read the documentation for more information"
        }
        kwargs = {
            "You can put additional settings here": "Read the documentation for more information"
        }

    def __init__(self):
        self.captcha = Configuration.Default.captcha
        self.captcha_public = Configuration.Default.captcha_public
        self.captcha_private = Configuration.Default.captcha_private
        self.discord_token = Configuration.Default.discord_token
        self.analytics = Configuration.Default.analytics
        self.discord_welcome_room = Configuration.Default.discord_welcome_room
        self.args = Configuration.Default.args
        self.kwargs = Configuration.Default.kwargs


def load_conf():
    with open("config.yaml", "rt") as f:
        return yaml.load(f, Loader=yaml.Loader)
