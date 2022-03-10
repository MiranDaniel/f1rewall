
#
# Version 2.0.0-alpha.1
#
import hashlib

from flask import Flask

from blueprints import gate
from blueprints import dash

from source import utils

from source import conf
from source.decorators import catch_goodbye
import threading


utils.check_os()
utils.check_setup()


configuration = conf.load_conf()

app = Flask(__name__)
app.register_blueprint(gate.gateway)
app.register_blueprint(dash.dashboard)


scrt = open("config.yaml","rt").read()+open("users.yaml","rt").read()
sha512 = hashlib.sha512()
sha512.update(scrt.encode('utf-8'))

app.secret_key = sha512.hexdigest()
# the app secret key is based on the sha512 hash of the combined configuration files
# since they are kept secret at all times this is a secret way of generating a
# secure key that will change (logging users out) when a password is changed


@catch_goodbye()
def run():
    threading.Thread(target=app.run, daemon=True).start()
    while True:
        input()


run()
