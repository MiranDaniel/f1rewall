make:
	apt-get update
	apt-get upgrade

	-apt-get install python3-dev
	-apt-get install python3-venv
	python3 -m venv ./.venv
	./.venv/bin/python3 -m pip install -r requirements.txt
