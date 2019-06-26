Tags: bash

# Docker

Docker provides containers, a kind of virtual environment, for your app to run on. Containers are create from images, blueprints of the environment. They are usually created from an pre-built os image provided by Docker Hub, followed by layers of instructions to install libraries or frameworks required by your app. These instructions are writen in `Dockerfile`.

A project usually has more than one app. With Docker, multiple apps can be run together with `docker-compose.yml` as the config file.

# Create the Template

You want to have a template app for quick start on future project. To create one, you first have to start with a pre-built os image and manually install all the required packages for your template app until you can successfully start it up. The steps (for an example project) includes:

1. Run `docker run -it ubuntu:18.04 bash`
1. Run `apt update`
1. Run `apt install -y ruby2.5` and install needed packages
1. Check latest version for rails (assuming it's 5.2.3) and bundler (assuming it's 2.0.2)
1. Run `gem install rails -v 5.2.3` and install needed packages
1. Run `gem install bundler -v 2.0.2` and install needed packages
1. Run `cd /home`
1. Run `rails new rails-app` and install needed packages
1. Run `bundle exec rails s` and install needed packages
1. Exit the container

Then you create the template source code, using the same specific version for the required packages.

After that, you write the instructions to `Dockerfile` and build the image. The steps (for the example project) includes:

1. Write `Dockerfile` to the app dir
1. Run `docker build -t rails-app .` from the app dir

When you want to update your template app with a newer version of its required packages, you will remove the old image and the old app dir, then repeat this process to create a new one.

Use this process for all other apps in the project and also write `docker-compose.yml`.

# Start a New Project

The steps:

1. Clone `docker-compose.yml`
1. Clone and rename the apps, adjust the ports in `docker-compose.yml`
1. Clone app dirs and rename them
