Tags: python, virtualenv

# What is Virtualenv

Virtualenv is a tool for switching your Python development environment. For instance, if you have both versions 2.6 and 2.7 of Python installed, only one of them is put as the `python` executable (the one you call when using command `python` on shell). If you want to switch to the other version, you can replace the binary in your `PATH`. Doing this is not very convenient, so virtualenv is created to quickly change your `PATH` instead, pointing to another excutable.

The tool also does the same for other Python packages, so it ends up creating whole development environments separated from each others.

# Installing Virtualenv

This example is writen based on:

- Ubuntu 18.04.1 LTS
- Python 3.6.7

Remember to check if things are already installed and can be skipped. You should also create a directory to store all the environments.

```shell
python3 --version
sudo apt install python3
pip3 --version
sudo apt install python3-pip
virtualenv --version
sudo pip3 install virtualenv
mkdir ~/.virtualenv
```

# Using Virtualenv

This example is writen based on:

- Virtualenv 16.1.0

Let's say you want to create an environment for Python 2, install Pelican package in it, then leave the environment:

```shell
cd  ~/.virtualenv/
mkdir hello-world
virtualenv -p python2 hello-world
source hello-world/bin/activate
pip install pelican
deactivate
```
