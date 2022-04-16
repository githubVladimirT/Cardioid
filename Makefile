build:
	pyinstaller --onefile master.py

setup:
	pip3 install -r requirements.txt

run:
	python3 master.py

