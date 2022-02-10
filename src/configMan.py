import yaml

with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        quit(1)


def check():
    if "dark_theme" not in config:
        print("!! Theme not defined")
    if "recaptcha" in config:
        if config["recaptcha"]["public"] == None:
            print("!! Recaptcha public key is not defined, exiting")
            quit(1)
        if config["recaptcha"]["private"] == None:
            print("!! Recaptcha private key is not defined, exiting")
            quit(1)
    else:
        print("!! Recaptcha config doesnt exist, exiting")
        quit(1)

    if "discord" in config:
        if config["discord"]["welcome_room"] == None:
            print("!! Discord welcome room not defined, exiting")
            quit(1)
        if config["discord"]["private"] == None:
            print("!! Discord private key is not defined, exiting")
            quit(1)
    else:
        print("!! Discord config doesnt exist, exiting")
        quit(1)

    if "server" in config:
        if config["server"]["port"] == None:
            print("!! Server port not defined, exiting")
            quit(1)
    else:
        print("!! Sever config not defined, exiting")
        quit(1)


def hasPro():
    return config["pro"] == True


def getPubkeys():
    return {
        "recaptcha": config["recaptcha"]["public"]
    }


def getPrivKeys():
    return {
        "recaptcha": config["recaptcha"]["private"],
        "discord": config["discord"]["private"]
    }


def getWelcomeRoom():
    return config["discord"]["welcome_room"]
