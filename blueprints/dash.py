from flask import Blueprint, render_template, request, redirect, session

from source import captcha
from source import conf
from source import utils
from source import analytics

utils.check_os()
utils.check_setup()

dashboard = Blueprint('dashboard', __name__,
                      template_folder='templates')

configuration = conf.load_conf()
users = conf.load_users()

a = analytics.Analytics()

@dashboard.route('/admin/logout')
def logout():
    session["userkey"] = ""
    session["username"] = ""
    args = configuration.args.copy()
    args["message"] = "Successfully logged out!"
    return render_template(
        "login.jinja2",
        captcha=configuration.captcha,
        public=configuration.captcha_public,
        args=args,
        kwargs=configuration.kwargs
    )


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
    session["username"] = data["username"]

    return redirect("/admin/dashboard")


@dashboard.route("/admin/dashboard/")
@dashboard.route("/admin/dash/")
@dashboard.route("/admin/")
@dashboard.route("/admin/dashboard/<path>")
@dashboard.route("/admin/dash/<path>")
@dashboard.route("/admin/<path>")
def dash(path=""):
    if "userkey" not in session:
        return redirect("/admin/login")
    check = users.check_cookie(session["userkey"])
    if check is True:
        args = configuration.args.copy()
        args["user"] = {
            "username": session["username"]
        }
        args["path"] = path
        if path == "analytics":
            args["analytics"] = {
                "users_24h": 0,  # TODO
                "users_total": 0
            }
        return render_template(
            "dashboard.html",
            captcha=configuration.captcha,
            public=configuration.captcha_public,
            args=args,
            kwargs=configuration.kwargs
        )
    else:
        return redirect("/admin/login")
