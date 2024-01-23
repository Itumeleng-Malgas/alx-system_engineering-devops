#!/usr/bin/env bash

wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

sudo gpg --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo gpg --export --armor B7B3B788A8D3785C | sudo apt-key add -

sudo apt update
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
