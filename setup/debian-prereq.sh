#!/bin/bash
echo "Checking for libmysqlclient-dev..."
CHECK=`dpkg -s libmysqlclient-dev | grep Status` 2>/dev/null
if [ "$CHECK" != "Status: install ok installed" ]; then
    echo "Hey there, we need to install this!"
    sudo apt-get update
    sudo apt-get install libmysqlclient-dev
else
    echo "Oh hey, it's installed!"
    echo "Jeorb done."
fi
