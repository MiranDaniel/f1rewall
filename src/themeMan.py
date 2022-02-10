import os
import json
import yaml
from . import configMan

directory = r'./templates'
conf = "src/themeconf.json"

conf = json.loads(open(conf, "rt").read())
themes = []

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        themes.append(filename.replace(".html", ""))

selected = configMan.getTheme()
if selected not in themes:
    print(f"Theme {selected} does not exist.")
if selected not in conf.keys():
    print(f"Theme {selected} does not have a valid config.")


if os.path.exists("theme.yaml"):
    with open("theme.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            configuration = config
        except yaml.YAMLError as exc:
            print(exc)
            quit(1)
else:
    with open("theme.yaml", "wt+") as w:
        w.write("# this is a configuration file for the frontend look\n")
        yaml.dump(conf[selected], w)
