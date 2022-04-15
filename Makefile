build:
	pip3 install -r requirements.txt && python3 -m pyinstaller --onefile master.py

setup:
	pip3 install -r requirements.txt

run:
	python3 master.py

