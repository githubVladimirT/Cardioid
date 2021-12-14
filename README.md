# Cardioid

## For run this application follow the instructions:

### 1. Install python (if you haven't already).

### 2. Run this commands (**Don't start as sudo!**):
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

### *. For add the background music, add music file to folder assets/music/ then in file [settings.py](https://github.com/githubVladimirT/Cardioid/blob/main/settings.py), finally paste path to file in the const "music_path" after char equals.

### For exit from app hit 'ESC' or 'Ctrl+w' or 'Ctrl+q' or 'Alt+F4'.
