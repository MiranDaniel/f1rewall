import yaml
import requests

import exceptions


def verifyRecaptcha(token, request, config):
    print(f"Verifying recaptcha {token[:15]}")
    recaptcha_url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {
        "secret": config["recaptcha"]["private"],
        "response": token,
        "remoteip": request.remote_addr,
    }
    response = requests.post(recaptcha_url, data=payload)
    result = response.json()
    return result


def generateInvite(config):
    print("Generating new invite!")
    resp = requests.post(
        f"https://discordapp.com/api/channels/{config['discord']['welcome_room']}/invites",
        headers={"Authorization": f"Bot {config['discord']['private']}"},
        json={"max_uses": 1, "unique": True, "max_age": 300},
    )
    i = resp.json()
    if resp.status_code != 200:
        raise exceptions.InviteGenerationError(i)
    if i.get("code"):
        print("Generated new invite!")
        return i["code"]

    raise exceptions.InviteGenerationError(i)


def verifyConfig(config):
    ok = True

    if "dark_theme" not in config:
        print("!! Theme not defined")
    if "recaptcha" in config:
        if config["recaptcha"]["public"] == None:
            print("!! Recaptcha public key is not defined, exiting")
            ok = False
        if config["recaptcha"]["private"] == None:
            print("!! Recaptcha private key is not defined, exiting")
            ok = False
    else:
        print("!! Recaptcha config doesnt exist, exiting")
        ok = False

    if "discord" in config:
        if config["discord"]["welcome_room"] == None:
            print("!! Discord welcome room not defined, exiting")
            ok = False
        if config["discord"]["private"] == None:
            print("!! Discord private key is not defined, exiting")
            ok = False
    else:
        print("!! Discord config doesnt exist, exiting")
        ok = False

    if "server" in config:
        if config["server"]["port"] == None:
            print("!! Server port not defined, exiting")
            ok = False
    else:
        print("!! Sever config not defined, exiting")
        ok = False

    if not ok:
        quit(1)
