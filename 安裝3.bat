@echo on
echo Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.4/python-3.11.4.exe -OutFile python-installer.exe"

echo Installing Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

timeout /t 5

echo Installing required Python packages...
pip install flask flask_login flask-sqlalchemy paho-mqtt

echo Cloning the GitHub repository...
powershell -Command "Invoke-WebRequest -Uri https://github.com/clre20/Earthquake-power-system-2024-Topics/archive/refs/heads/main.zip -OutFile Earthquake-power-system-2024-Topics.zip"
powershell -Command "Expand-Archive -Path Earthquake-power-system-2024-Topics.zip -DestinationPath ."
del Earthquake-power-system-2024-Topics.zip

echo Installation and download complete!
pause
