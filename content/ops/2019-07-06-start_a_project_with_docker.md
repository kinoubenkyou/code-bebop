Tags: bash, docker

# Docker

Docker provides containers, a kind of virtual environment, for your project to run on. Containers are create from images, blueprints of the environments. They are usually created from a pre-built OS image provided by Docker Hub, followed by layers of instructions to install libraries or frameworks depended by the applications of your project. These instructions are writen to `Dockerfile`.

A project usually has more than one application running together. Each of them ,when running in their own separated containers, are called services. All services can be configured in a single `docker-compose.yml`.

A typical project structure would include the project root containing a `docker-compose.yml` and one/many application directories. Each of these directories would contain their own `Dockerfile`.

# Create and Running Docker Containers

1. Create the project directory
1. Create the applications, usually by using commands provided by frameworks. This would create the applications' directory and their initial codes
1. Write a `Dockerfile` to each application's root (more details later)
1. Write a `docker-compose.yml` to your project root
1. Run your project

# Write a Dockerfile

The idea is to write one by one line of instruction and try building the image with

```bash
docker build -t <service-name> .
```

If it succeeds, the build for next line will continue on the lastest image without rebuilding from the start. If you change an old instruction, the image will have to rebuild from that point. The old image will be tagged to `<none>` and you can safely remove it.

# Example

Example for `docker-compose.yml` and `Dockerfile`:

[https://github.com/kinoubenkyou/docker-example](https://github.com/kinoubenkyou/docker-example)
