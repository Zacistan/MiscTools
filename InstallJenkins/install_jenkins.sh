#!/usr/bin/env bash
# Must be ran as sudo

# Check if Java is installed
if ! type -p java; then
    echo "Java is not installed."
    exit 1
fi

# Jenkins install steps
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list
apt-get update
apt-get install jenkins