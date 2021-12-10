# Cardioid

## For run this application follow the instructions:

### 1. install python (if you haven't already).

### 2. run this commands:
``` bash
# Check existence of command "gh". Because "gh clone" is faster then "git clone"
if ! command -v gh &> /dev/null
then
	git clone https://github.com/githubVladimirT/Cardioid.git ; cd Cardioid ; pip3 install -r requirements.txt ; python3 master.py
else
	gh repo clone githubVladimirT/Cardioid ; cd Cardioid ; pip3 install -r requirements.txt ; python3 master.py
fi
```

### 3. If you want change settings edit consts if file [settings.py](https://github.com/githubVladimirT/Cardioid/blob/main/settings.py).

### *. For add the background music add music file to assets/music/ and in file [settings.py](https://github.com/githubVladimirT/Cardioid/blob/main/settings.py) then paste path to file in the const "path_to_music" after char equals.
