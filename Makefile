setup:
	pip install -r requirements.txt

run:
	python main.py

push:
	echo > main.log
	git add .
	git commit -s -m "update"
	git push
	
pylint:
	pylint `git ls-files '*.py'` --disable=C,W > pylint_stat.json

