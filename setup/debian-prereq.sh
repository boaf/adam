#!/bin/bash
# ERMAHGERD THIS NEEDS WERK
sudo apt-get update
sudo apt-get install python-dev libmysqlclient-dev

#REQS[0]="python-dev"
#REQS[1]="libmysqlclient-dev"
#
#echo "Checking our dependencies"
#for item in "$REQS"; do
#    checkItem=`dpkg -s $item | grep Status` 2>/dev/null
#    if [ "$checkItem" != "Status: install ok installed" ]; then
#    sudo apt-get update
#    sudo apt-get install libmysqlclient-dev
#    else
#    fi
#done
echo "All good!"
echo "Enter virtualenv and run:"
echo ". setup/debian-venv-setup.sh"
