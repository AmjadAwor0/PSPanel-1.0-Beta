#!/bin/bash
echo "Welcome to PSPanel Setup"
echo "Loading..."
cp files/pspanel /bin/
chmod +x /bin/pspanel
mkdir /opt/pspanel/
cp files/auto /opt/pspanel/
cp files/psedit.py /opt/pspanel/
cp files/help /opt/pspanel/
cp files/PSPanel.py /opt/pspanel/
cd /opt/pspanel/
touch errors
mkdir payloads
mkdir projects
echo "Setup finished!"
echo "You can delete all these file now."
