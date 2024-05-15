from gevent.pywsgi import WSGIServer
from app import app
import yaml

with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        quit(1)

print(f"Serving on port {config['server']['port']}")

http_server = WSGIServer(("", config["server"]["port"]), app)
http_server.serve_forever()
