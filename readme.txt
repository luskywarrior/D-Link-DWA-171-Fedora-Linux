This file is an adaptation of a pre-existing driver for the D-Link 171 wireless adapter for Ubuntu. 
From it, I modified commands like sudo apt to sudo dnf, added a check for previous driver versions, and searched for an updated driver version.
you can see the original file in:
(https://github.com/CarlosSenobio/d-link-dwa-171-wifi-adapter-automatic-driver-installer?tab=readme-ov-file)

How to use
git clone 
# Installing Dependencies (you need colorama)
pip3 install -r requirements.txt 
# Run the Script
python3 main.py
