#!/bin/bash
echo "Upgrading distribute..."
pip install --upgrade distribute
echo "Installing requirements..."
pip install -r requirements.txt
echo "All done!"
