import multiprocessing

from flask import Blueprint, render_template, abort, request, redirect
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


@dashboard.route('/admin/login')
def login():
    return render_template(
        "login.jinja2",
        captcha=configuration.captcha,
        public=configuration.captcha_public,
        args=configuration.args,
        kwargs=configuration.kwargs
    )
