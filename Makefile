make:
	apt-get update -y
	apt-get upgrade -y

	-apt-get install python3-dev -y
	-apt-get install python3-venv -y
	python3 -m venv ./.venv
	./.venv/bin/python3 -m pip install -r requirements.txt
