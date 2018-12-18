Tags: python, virtualenv

# What is Virtualenv

Virtualenv is a tool for switching Python development environment. For instance, both versions 2.6 and 2.7 of Python are installed, only one of them is put as Python executable (the one called when using command `python` on shell). To switch ther version, the binary in `PATH` can be replaced. Doing this is not very convenient, so virtualenv is created to quickly change `PATH` instead, pointing to another excutable.

The tool also does the same for other Python packages, so it ends up creating whole development environments separated from each others.

# Installing Virtualenv

This example is writen based on:

- Ubuntu 18.04.1 LTS
- Python 3.6.7

Check if Python and Pip are already installed and can be skipped:

```bash
python3 --version
sudo apt install python3
pip3 --version
sudo apt install python3-pip
```

Check if virtualenv is installed and can be skipped:

```bash
virtualenv --version
sudo pip3 install virtualenv
```

Create a directory to store all the environments:

```bash
mkdir ~/.virtualenv
```

# Using Virtualenv

This example is writen based on:

- Virtualenv 16.1.0

The following steps create an environment for Python 2, install Pelican package in it, then leave the environment:

Create an environment, such as for a project name hello-world, with Python 2:

```bash
cd  ~/.virtualenv/
mkdir hello-world
virtualenv -p python2 hello-world
```

Switch to the environment:

```bash
source hello-world/bin/activate
```

Install a package, such as Pelican, in the environment:

```bash
pip install pelican
```

Switch out of the environment:

```bash
deactivate
```
