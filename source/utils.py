from sys import platform
import os
from .conf import Configuration
from blessed import Terminal


term = Terminal()


def goodbye():
    print("\n" * 2)
    print(" Goodbye!")
    print(term.green(
        f" f1rewall is {term.bold('free and opensource')}, please consider donating to help the project development!"))
    print(term.cyan(" https://github.com/MiranDaniel/f1rewall#donations-3"))


def check_os():
    if platform == "linux" or platform == "linux2":
        pass
    elif platform == "darwin":
        print("Your operating system is not officially supported, proceed with caution!")
    elif platform == "win32":
        print("Your operating system is not officially supported, proceed with caution!")


def check_setup():
    if not os.path.exists("config.yaml"):
        print("The f1rewall config file do not exist.")
        print("Run setup.py to create them")
        quit(2)  # No such file or directory


def check_config(conf: Configuration):
    result = [
        conf.captcha == conf.Default.captcha,
        conf.analytics == conf.Default.analytics,
        conf.discord_token == conf.Default.discord_token,
        conf.captcha_public == conf.Default.captcha_public,
        conf.captcha_private == conf.Default.captcha_private,
    ]
    if True not in result:
        return True
    else:
        print("Invalid configuration!")
        print("Run setup.py to recreate it")
