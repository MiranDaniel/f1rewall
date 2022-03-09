from .utils import goodbye
import sys


def catch_goodbye():
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except KeyboardInterrupt:
                goodbye()
                sys.exit(0)

        return applicator

    return decorate
