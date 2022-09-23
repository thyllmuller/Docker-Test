# Docker-Test
 Docker Learning and Testing Environment

## Installation
Docker installer can be found at: https://docs.docker.com/get-docker/

## Usage
Once docker has been installed, the docker images can be built and ran via these terminal commands:

```bash
# To create the requirements file:
    pip freeze > requirements.txt
# To build the docker image:
    docker build -t fast2 .
# To run the image:
    docker run -p 80:80 fast
```