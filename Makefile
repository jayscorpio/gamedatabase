install:
	pip install -r requirements.txt

version:
	python main.py --version

start:
	python main.py --verbose

build:
	python main.py --buildonly

import:
	python main.py --importonly

test:
	python main.py --dryrun --verbose
