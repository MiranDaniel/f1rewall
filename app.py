"""
Copyright 2021 MiranDaniel
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from flask import Flask, render_template, request, redirect
import yaml
import requests
from pro import Pro
import threading
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per second"]
)

with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        quit(1)


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

if "pro" in config:
    pro_enabled = config["pro"]
else:
    pro_enabled = False

pro = Pro(enabled=pro_enabled)


def recaptcha(token):
    print(f"Verifying recaptcha {token[:15]}")
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': config["recaptcha"]["private"],
        'response': token,
        'remoteip': request.remote_addr,
    }
    response = requests.post(recaptcha_url, data=payload)
    result = response.json()
    return result


def invite():
    print("Generating new invite!")
    resp = requests.post(
        'https://discordapp.com/api/channels/{}/invites'.format(
            config["discord"]["welcome_room"]),
        headers={'Authorization': 'Bot {}'.format(
            config["discord"]["private"])},
        json={'max_uses': 1, 'unique': True, 'max_age': 300}
    )
    i = resp.json()
    # error handling for invite creation
    if (i.get('code')):
        print("Generated new invite!")
    else:
        print(i)
    return i["code"]


theme = "text-dark border-dark" if config["dark_theme"] else "text-light border-light"
border = "border-dark" if config["dark_theme"] else ""
catpcha_theme = "dark" if config["dark_theme"] else "light"


@app.route("/")  # main function
@limiter.limit("10 per second")
def index():
    threading.Thread(target=pro.visit).start()
    key = request.args.get('key')  # get key parameter from URL
    if key:  # if key set
        r = recaptcha(key)  # confirm captcha
        if r["success"]:  # if ok
            print(f"Recaptcha {key[:30]} verified!")
            i = invite()  # generate new invite
            # redirect user to new invite
            return redirect(f"https://discord.gg/{i}")
        else:  # if captcha invalid
            print(f"Recaptcha {key[:30]} failed!")
            # return error page
            return render_template("index.html", public=config["recaptcha"]["public"], failed=True, theme=theme, border=border, catpcha_theme=catpcha_theme)
    # if not key
    # return normal page
    return render_template("index.html", public=config["recaptcha"]["public"], failed=False, theme=theme, border=border, catpcha_theme=catpcha_theme)


@app.route("/admin/")
@app.route("/admin/login")
@limiter.limit("2 per second")
def _login():
    return render_template("admin/login.html", public=config["recaptcha"]["public"])


@app.route("/api/login", methods=["POST"])
@limiter.limit("6 per minute")
def api_login():
    return "ok"
