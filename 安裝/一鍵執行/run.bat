@echo on
pip install flask flask_login flask-sqlalchemy paho-mqtt
timeout /t 5
powershell -Command "Invoke-WebRequest -Uri https://github.com/clre20/Earthquake-power-system-2024-Topics/archive/refs/heads/main.zip -OutFile Earthquake-power-system-2024-Topics.zip"
powershell -Command "Expand-Archive -Path Earthquake-power-system-2024-Topics.zip -DestinationPath ."
del Earthquake-power-system-2024-Topics.zip
cd /Earthquake-power-system-2024-Topics-app.py/Web
timeout /t 5
python Earthquake-power-system-2024-Topics-app.py/Web/app.py
pause