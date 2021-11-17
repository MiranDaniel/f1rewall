make:
	python3 -m venv ./.venv
	./.venv/bin/python3 -m pip install -r requirements.txt
	./.venv/bin/python3 -m pip install -U git+https://github.com/Pycord-Development/pycord