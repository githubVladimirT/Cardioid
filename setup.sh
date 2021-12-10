chmod +x setup.sh

function runCardioid
{
	python3 master.py
}

if ! command -v gh &> /dev/null
then
	git clone https://github.com/githubVladimirT/Cardioid.git ; cd Cardioid ; pip3 install -r requirements.txt ; runCardioid
else
	gh repo clone githubVladimirT/Cardioid ; cd Cardioid ; pip3 install -r requirements.txt ; runCardioid
fi
