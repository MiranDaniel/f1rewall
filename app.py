from flask import Flask, render_template, request, redirect
import yaml
import requests

with open("config.yaml","r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        quit(1)

def recaptcha(token):
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': config["recaptcha"]["private"],
        'response': token,
        'remoteip': request.remote_addr,
    }
    response = requests.post(recaptcha_url, data = payload)
    result = response.json()
    return result

def invite():
    resp = requests.post(
        'https://discordapp.com/api/channels/%s/invites' % config["discord"]["welcome_room"], 
        headers={'Authorization': 'Bot %s' % config["discord"]["private"]},
        json={'max_uses': 1, 'unique': True, 'expires': 300}
    )
    i = resp.json()
    return i["code"]

app = Flask(__name__)

theme = "text-dark border-dark" if config["dark_theme"] else "text-light border-light"
border = "border-dark" if config["dark_theme"] else ""
catpcha_theme = "dark" if config["dark_theme"] else "light"

@app.route("/")
def index():
    key = request.args.get('key')
    if key:
        r = recaptcha(key)
        if r["success"]:
            i = invite()
            return redirect(f"https://discord.gg/{i}")
        else:
            return render_template("index.html", public=config["recaptcha"]["public"], failed=True, theme=theme, border=border, catpcha_theme=catpcha_theme)

    return render_template("index.html", public=config["recaptcha"]["public"], failed=False, theme=theme, border=border, catpcha_theme=catpcha_theme)
