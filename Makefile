install:
	pip install -r requirements.txt

version:
	python main.py --version

start:
	python main.py --verbose

startself:
	python main.py --verbose --self

startatlas:
	python main.py --verbose --atlas

build:
	python main.py --buildonly

import:
	python main.py --importonly

importself:
	python main.py --importonly --self

importatlas:
	python main.py --importonly --atlas

test:
	python main.py --dryrun --verbose
