from flask import Blueprint, render_template
from source import conf
from source import utils


utils.check_os()
utils.check_setup()

gateway = Blueprint('gateway', __name__,
                    template_folder='templates')

configuration = conf.load_conf()


@gateway.route('/')
def gateway_fun():
    print(configuration.captcha)
    return render_template(
        "index.jinja2",
        captcha=configuration.captcha,
        public=configuration.captcha_public,
        args=configuration.args,
        kwargs=configuration.kwargs
    )
