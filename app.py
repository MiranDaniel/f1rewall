"""
Copyright 2021-2022 MiranDaniel


The Software is provided to you by the Licensor under
the License, as defined below, subject to the following
condition.

Without limiting other conditions in the
License, the grant of rights under the License will not
include, and the License does not grant to you, the
right to Sell the Software.

For purposes of the
foregoing, “Sell” means practicing any or all of the
rights granted to you under the License to provide to
third parties, for a fee or other consideration
(including without limitation fees for hosting or
consulting/ support services related to the Software), a
product or service whose value derives, entirely or
substantially, from the functionality of the Software.
Any license notice or attribution required by the
License must also include this Commons Cause License
Condition notice.


THE SOFTWARE IS PROVIDED "AS IS",
WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from flask import Flask, render_template, request, redirect
import yaml
import requests

with open("config.yaml","r") as stream:
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

def recaptcha(token):
    print(f"Verifying recaptcha {token[:15]}")
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
    print("Generating new invite!")
    resp = requests.post(
        'https://discordapp.com/api/channels/{}/invites'.format(config["discord"]["welcome_room"]), 
        headers={'Authorization': 'Bot {}'.format(config["discord"]["private"])},
        json={'max_uses': 1, 'unique': True, 'max_age': 300}
    )
    i = resp.json()
    # error handling for invite creation
    if (i.get('code')):
        print("Generated new invite!")
    else:
        print(i)
    return i["code"]

app = Flask(__name__)

theme = "text-dark border-dark" if config["dark_theme"] else "text-light border-light"
border = "border-dark" if config["dark_theme"] else ""
catpcha_theme = "dark" if config["dark_theme"] else "light"


@app.route("/") # main function
def index():
    key = request.args.get('key') # get key parameter from URL
    if key: # if key set
        r = recaptcha(key) # confirm captcha
        if r["success"]: # if ok
            print(f"Recaptcha {key[:30]} verified!")
            i = invite() # generate new invite
            return redirect(f"https://discord.gg/{i}") # redirect user to new invite
        else: # if captcha invalid
            print(f"Recaptcha {key[:30]} failed!")
            return render_template("index.html", public=config["recaptcha"]["public"], failed=True, theme=theme, border=border, catpcha_theme=catpcha_theme) # return error page
    # if not key
    return render_template("index.html", public=config["recaptcha"]["public"], failed=False, theme=theme, border=border, catpcha_theme=catpcha_theme) # return normal page
