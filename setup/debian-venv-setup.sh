#!/bin/bash
DIR="$(dirname ${BASH_SOURCE[0]})"
echo "Upgrading distribute..."
pip install --upgrade distribute
echo "Installing requirements..."
pip install -r $DIR/requirements.txt
echo "All done!"
