import multiprocessing

from flask import Blueprint, render_template, abort, request, redirect
from source import conf
from source import utils
from source import captcha
from source import invites

import threading

utils.check_os()
utils.check_setup()

gateway = Blueprint('gateway', __name__,
                    template_folder='templates')

configuration = conf.load_conf()
ip = invites.InvitePool()
ip.fill()


@gateway.route('/')
def gateway_fun():
    return render_template(
        "index.jinja2",
        captcha=configuration.captcha,
        public=configuration.captcha_public,
        args=configuration.args,
        kwargs=configuration.kwargs
    )


@gateway.route("/verify/<code>")
@gateway.route("//verify/<code>")
def verify_fun(code=""):
    if code == "":
        return abort(418)

    h = captcha.handle(
        code,
        ip=request.remote_addr
    )
    if h is True:
        def wrapper(invite):
            invite["code"] = ip.get()

        manager = multiprocessing.Manager()
        invite = manager.dict()

        p = threading.Thread(target=wrapper, args=(invite,))
        p.start()
        p.join(15)

        if p.is_alive():
            print("Killing alive process, stuck")

        if "code" not in invite:
            print("Ratelimit")
            return redirect("/")

        return redirect(f"https://discord.gg/{invite['code']}")
