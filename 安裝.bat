@echo on
powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe -OutFile python-installer.exe"
timeout /t 5
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
powershell -Command "Invoke-WebRequest -Uri 'https://clre20.github.io/run_as_admin.ps1' -OutFile 'C:\Users\C4\Desktop\run_as_admin.ps1'"
powershell -Command "Invoke-WebRequest -Uri 'https://clre20.github.io/e2.bat' -OutFile 'C:\Users\C4\Desktop\e2.bat'"
powershell -ExecutionPolicy Bypass -File "C:\Users\C4\Desktop\run_as_admin.ps1"
pause