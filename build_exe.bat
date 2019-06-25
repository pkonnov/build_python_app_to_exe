@echo off
cd %~1
"C:\Program Files\7-Zip\7z.exe" e *.tar.gz
"C:\Program Files\7-Zip\7z.exe" x *.tar
set targetDir="dir /a:d /b"
FOR /F "dir=*" %%i IN (' %targetDir% ') DO SET X=%%i
cd %X%
pyinstaller -F -w __main.py --name %~2
"C:\Program Files\7-Zip\7z.exe" a -sdel %~2.zip *
