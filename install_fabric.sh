#!/bin/bash

# Check if virtualenv is installed
if ! command -v virtualenv &>/dev/null; then
    echo "Installing virtualenv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
fi

# Create a virtual environment (replace 'myenv' with your desired environment name)
virtualenv -p python3 myenv

# Activate the virtual environment
source myenv/bin/activate

# Install Fabric dependencies
echo "Installing Fabric dependencies..."
pip3 uninstall -y Fabric
sudo apt-get install -y libffi-dev libssl-dev build-essential python3.4-dev libpython3-dev
pip3 install pyparsing appdirs setuptools==40.1.0 cryptography==2.8 bcrypt==3.1.7 PyNaCl==1.3.0

# Install Fabric for Python 3
pip3 install Fabric3==1.14.post1

# Verify the installation
echo "Fabric version:"
fab --version

# Deactivate the virtual environment
deactivate

echo "Fabric for Python 3 has been installed and configured."
