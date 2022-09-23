# skipped a step for syntax declaration, although this is officially flagged as optional
# mostly seems to be relevant if utilising archaic images or archaic docker versions

# specifying which python base image to use:
FROM python:3.10

# Telling Docker to use this path as the default location for all subsequent commands.
WORKDIR /code

# Important to get the requirements file in before the pip install command, so we copy the requirements file in.
# questioning whether I need to specify /code for the destination (shouldn't in theory).
COPY ./requirements.txt /code/requirements.txt

# RUN executes a command, here the pip install:
RUN pip install --no-cache-dir -r /code/requirements.txt
# --no-cache-dir. Reason for docker usage is really contained down to making the docker image as small as possible.
# No other great reason for it as far as i know.

# here we copy everything from the app folder into the image, again questioning if I need /code.
COPY ./app /code/app

# In order to instruct the docker what to run when the image is executed, we use the CMD command:
CMD ["uvicorn","app.main:app", "--host=0.0.0.0", "--port=80"]
# here we run the fast api instanced "app" via uvicorn referring to it
# Uvicorn is an ASGI (async server gateway interface) web server implementation for Python.
# "(simplified) the binding element that handles the web connections from the browser or
# api client and then allows FastAPI to serve the actual request" --more on this: https://stackoverflow.com/questions/71435960/what-is-the-purpose-of-uvicorn
# Note that we need to make the application externally visible (i.e. from outside the container) by specifying --host=0.0.0.0
# also, need to specify port via --port and the corresponing number 80
# multiple way of doing this such as "--host", "0.0.0.0" and "--port", "80" - there are nuances to this I think.