#!/bin/bash

if [ -n "$1 $2" ]
then
cd $1 &&
unzip *.zip -d ./tmp && 
echo "Archive unzipped" &&
echo "Install pyinstaller" &&
cd ./tmp/*/ && pip install pyinstaller &&
pyinstaller -F *.py --name $2 &&
touch readme.txt &&
echo "exe file is in the dist folder" && 
zip $2.zip * &&
echo "##### Archive $2 ready #####"
else
echo "Enter the path to the file and name project"
fi

