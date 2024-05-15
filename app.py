"""
Copyright MiranDaniel <me@mirandaniel.com>


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

import exceptions
from utils import verifyRecaptcha, generateInvite, verifyConfig

with open("config.yaml", "r") as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)
        quit(1)
    else:
        verifyConfig(config)

app = Flask(__name__)

theme = "text-dark border-dark" if config["dark_theme"] else "text-light border-light"
border = "border-dark" if config["dark_theme"] else ""
catpcha_theme = "dark" if config["dark_theme"] else "light"


@app.route("/")
def index():
    key = request.args.get("key")
    if key:  # User has submitted a captcha
        r = verifyRecaptcha(key, request, config)
        if r.get("success"):  # Captcha is OK
            print(f"Recaptcha {key[:30]} verified!")
            inviteCode = generateInvite(config)
            return redirect(f"https://discord.gg/{inviteCode}")
        else:  # Captcha failed
            print(f"Recaptcha {key[:30]} failed!")
            # Return error page
            return render_template(
                "index.html",
                public=config["recaptcha"]["public"],
                failed="Invalid captcha, try again",
                theme=theme,
                border=border,
                catpcha_theme=catpcha_theme,
            )

    return render_template(
        "index.html",
        public=config["recaptcha"]["public"],
        failed=None,
        theme=theme,
        border=border,
        catpcha_theme=catpcha_theme,
    )  # Return normal page


@app.errorhandler(500)
def internalError(error):
    return render_template(
        "index.html",
        public=config["recaptcha"]["public"],
        failed="Internal server error, please try again later",
        theme=theme,
        border=border,
        catpcha_theme=catpcha_theme,
    )


@app.errorhandler(404)
def notFound(error):
    return render_template(
        "index.html",
        public=config["recaptcha"]["public"],
        failed=None,
        theme=theme,
        border=border,
        catpcha_theme=catpcha_theme,
    )
