@echo on
powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe -OutFile python-installer.exe"
timeout /t 5
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0