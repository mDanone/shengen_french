#!/bin/sh
# Run with sudo
rm -rf driver/
mkdir driver
wget -P driver/ "https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip"
unzip driver/chromedriver_linux64.zip -d driver/
rm -rf driver/chromedriver_linux64.zip