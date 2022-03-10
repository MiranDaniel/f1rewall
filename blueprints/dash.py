import hashlib
import multiprocessing

from flask import Blueprint, render_template, abort, request, redirect, session
from source import conf
from source import utils
from source import captcha
from source import invites

import threading

utils.check_os()
utils.check_setup()

dashboard = Blueprint('dashboard', __name__,
                      template_folder='templates')

configuration = conf.load_conf()
users = conf.load_users()


@dashboard.route('/admin/logout')
def logout():
    session["userkey"] = ""
    return str("Successfully logged out!")


@dashboard.route('/admin/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template(
            "login.jinja2",
            captcha=configuration.captcha,
            public=configuration.captcha_public,
            args=configuration.args,
            kwargs=configuration.kwargs
        )
    data = dict(request.form)
    h = captcha.handle(
        data["g-recaptcha-response"],
        request.remote_addr
    )
    if h is False:
        args = configuration.args.copy()
        args["message"] = "Invalid captcha"
        return render_template(
            "login.jinja2",
            captcha=configuration.captcha,
            public=configuration.captcha_public,
            args=args,
            kwargs=configuration.kwargs
        )
    result = users.check_login(data["username"], data["password"])
    if result is False:
        args = configuration.args.copy()
        args["message"] = "Invalid username or password"
        return render_template(
            "login.jinja2",
            captcha=configuration.captcha,
            public=configuration.captcha_public,
            args=args,
            kwargs=configuration.kwargs
        )
    session["userkey"] = users.out_key(data["username"])

    return redirect("/admin/dashboard")


@dashboard.route("/admin/dashboard")
@dashboard.route("/admin/dash")
@dashboard.route("/admin")
def dash():
    if "userkey" not in session:
        return redirect("/admin/login")
    check = users.check_cookie(session["userkey"])
    if check is True:
        return render_template(
            "dashboard.jinja2",
            captcha=configuration.captcha,
            public=configuration.captcha_public,
            args=configuration.args,
            kwargs=configuration.kwargs
        )
    else:
        return redirect("/admin/login")
