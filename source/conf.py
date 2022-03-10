import bcrypt
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


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Users:
    def __init__(self):
        self.users = [

        ]

    def add_user(self, username, password):
        self.users.append(
            User(
                username,
                bcrypt.hashpw(password, bcrypt.gensalt(12))  # hash password
            )
        )

    def remove_user(self, username):
        match = [i for i in self.users if i.username == username]
        for i in match:
            self.users.remove(i)

    def check_login(self, username, password):
        match = [i for i in self.users if i.username == username]

        if len(match) < 1:
            return False

        match = match[0]

        return bcrypt.checkpw(password, match.password)


def load_conf():
    with open("config.yaml", "rt") as f:
        return yaml.load(f, Loader=yaml.Loader)


def load_users():
    if os.path.exists("users.yaml"):
        with open("users.yaml", "rt") as f:
            return yaml.load(f, Loader=yaml.Loader)
    else:
        return Users()


def save_users(data):
    with open("users.yaml", "wt+") as f:
        yaml.dump(data, f)
