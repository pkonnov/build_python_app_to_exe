@echo off
set nameTargetArchive=%1
"C:\Program Files\7-Zip\7z.exe" e %nameTargetArchive%.tar.gz
"C:\Program Files\7-Zip\7z.exe" x %nameTargetArchive%.tar
cd %nameTargetArchive%
pyinstaller -F -w __main.py --name %2
cd %nameTargetArchive%/
cd dist/
move %2.exe ../
cd ../
"C:\Program Files\7-Zip\7z.exe" a -sdel %2.zip %2.exe
rmdir __pycache__ build dist /s /q
del __main.py *.spec
