#!/bin/bash

# Get the dependencies for showing a daily message
sudo apt update && sudo apt install fortune-mod lolcat

# Copy files to the appropriate places:
cp .bashrc .bash_aliases .vimrc ~
mkdir -p ~/.config
cp -r kitty ~/.config
