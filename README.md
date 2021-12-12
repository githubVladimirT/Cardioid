# Cardioid

## For run this application follow the instructions:

### 1. install python (if you haven't already).

### 2. run this commands:
``` bash
# Check existence of command "gh". Because "gh clone" is faster then "git clone"
if ! command -v gh &> /dev/null
then
	git clone https://github.com/githubVladimirT/Cardioid.git # Clone repo
	cd Cardioid # Change dirictory to cloned
	pip3 install -r requirements.txt # Install or update modules
	chmod +x master.py
	./master.py # Run Cardioid
else
	gh repo clone githubVladimirT/Cardioid # Clone repo
	cd Cardioid # Change dirictory to cloned
	pip3 install -r requirements.txt # Install or update modules
	chmod +x master.py
	./master.py # Run Cardioid
fi
```

### 3. If you want change settings edit consts if file [settings.py](https://github.com/githubVladimirT/Cardioid/blob/main/settings.py).

### *. For add the background music add music file to assets/music/ and in file [settings.py](https://github.com/githubVladimirT/Cardioid/blob/main/settings.py) then paste path to file in the const "path_to_music" after char equals.

### For exit from app hit 'ESC' or 'Ctrl+w' or 'Ctrl+q' or 'Alt+F4'.
