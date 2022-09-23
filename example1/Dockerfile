# Dockerfile, Image, Container
# A Dockerfile is simply a text-based script of instructions that is used to create a container image.
#


FROM python:3.10

# The ADD command is used to copy files/directories into a Docker image.
ADD main.py .

RUN pip install requests beautifulsoup4

CMD  ["python", "./main.py"]


# to build: "docker build -t fast ."
# to run: "docker run fast"

# more reading:
# https://docs.docker.com/language/python/build-images/
# https://docs.docker.com/get-started/02_our_app/