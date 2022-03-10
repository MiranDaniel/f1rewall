import yaml
import os
from blessed import Terminal
from pwinput import pwinput
from source.conf import Configuration
from source import conf
from source.decorators import catch_goodbye
from source.utils import goodbye

term = Terminal()


@catch_goodbye()
def generate_config(force=False, conf=None):
    if conf == None:
        conf = Configuration()
    print("Generating config files")
    if os.path.exists("config.yaml") is False or force:
        with open("config.yaml", "w+") as f:
            yaml.dump(
                conf,
                f
            )
            print("Config files successfully created!")
    else:
        print("Config files already exist, would you like to overwrite them? Y/N")
        i = input("-- ")
        if i.lower() == "y":
            print("Overwriting...")
            generate_config(force=True, conf=conf)
        else:
            print("Exiting config generation...")
            return


@catch_goodbye()
def interactive_config():
    conf = Configuration()
    while conf.captcha == Configuration.Default.captcha:
        print("Would you like to use Google Recaptcha or hCaptcha? G/H")
        i = input("-- ")
        if i.lower() == "g":
            conf.captcha = "recaptcha"
            break
        elif i.lower() == "h":
            conf.captcha = "hcaptcha"
            break
        else:
            print("Invalid option")

    print("Input your captcha public key: ")
    i = input()
    conf.captcha_public = i
    print("Input your captcha private key: ")
    i = pwinput(mask="*", prompt="")
    conf.captcha_private = i
    print("Input your Discord bot token: ")
    i = pwinput(mask="*", prompt="")
    conf.discord_token = i

    print("Input your Discord welcome room ID")
    i = input("-- ")
    conf.discord_welcome_room = i

    while conf.analytics == Configuration.Default.analytics:
        print("Would you like to enable f1rewall analytics? Y/N")
        i = input("-- ")
        if i.lower() == "y":
            conf.analytics = True
            break
        elif i.lower() == "n":
            conf.analytics = False
            break
        else:
            print("Invalid option")

    generate_config(conf=conf)
    goodbye()


@catch_goodbye()
def manage_users():
    users = conf.load_users()
    print(term.gray100("  What would you like to do?"))
    print("   1. List users")
    print("   2. Add new user")
    print("   3. Remove user")
    print("   0. Exit")

    i = input("\n-- ")
    try:
        i = int(i)
    except ValueError:
        manage_users()

    if i == 1:
        print(f"There are {len(users.users)} registered users")
        print("index | username | password")
        for index, user in enumerate(users.users):
            print(f"[{index}] | {user.username} | {user.password}")
        print()
        manage_users()
    elif i == 2:
        print("Enter username: ")
        username = input()
        print("Enter password: ")
        password = pwinput(mask="*", prompt="")
        users.add_user(username, password)
        conf.save_users(users)
        print()
        manage_users()
    elif i == 3:
        print("Enter username: ")
        username = input()
        users.remove_user(username)
        conf.save_users(users)
        print()
        manage_users()
    elif i == 0:
        goodbye()
        quit(0)
    else:
        manage_users()


@catch_goodbye()
def welcome():
    print(term.home + term.clear + term.move_y(0))
    print(term.black_on_orange(' Welcome to f1rewall setup!' + " " * (term.width - 28)))
    print(term.gray100("  What would you like to do?"))
    print("   1. Generate settings file (manual setup)")
    print("   2. Run interactive setup " + term.green("[recommended]"))
    print("   3. Manage users (f1rewall analytics access)")
    print("   0. Exit")

    i = input("\n-- ")
    try:
        i = int(i)
    except ValueError:
        welcome()

    if i == 1:
        generate_config()
    elif i == 2:
        interactive_config()
    elif i == 3:
        manage_users()
    elif i == 0:
        goodbye()
        quit(0)
    else:
        welcome()


if __name__ == "__main__":
    welcome()
