Tags: bash, python, pip, virtualenv

# What is Virtualenv

Virtualenv is a tool for switching Python development environment. When an environment is activated, the tools help putting both Python and its packages of a particular version into a separated location, as well as adding this location into `PATH`.

# Install Virtualenv

This example is writen based on:

- Ubuntu 18.04.1 LTS

Check if virtualenv is installed and can be skipped:

```bash
virtualenv --version
sudo apt install virtualenv
```

Create a directory to store all the environments:

```bash
mkdir ~/.virtualenv
```

# Use Virtualenv

This example is writen based on:

- Virtualenv 16.1.0

Check if Python 2 are already installed and can be skipped:

```bash
python2 --version
sudo apt install python2
```

Create an environment, named hello-world for example, with Python 2:

```bash
cd  ~/.virtualenv/
mkdir hello-world
virtualenv -p python2 hello-world
```

Switch to the environment, the command line will be prepended with `(hello-world)`:

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
