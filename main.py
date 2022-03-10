
#
# Version 2.0.0-alpha.1
#


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


@catch_goodbye()
def run():
    threading.Thread(target=app.run, daemon=True).start()
    while True:
        input()


run()
