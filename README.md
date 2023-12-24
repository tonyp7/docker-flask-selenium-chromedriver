# Containerized Selenium/Chromedriver running on Python and Flask 
 
This is a docker image that comes pre-installed with a Python `Flask` web application that can run `Selenium` with `Chromedriver`.

# Why?

I needed to do some automated tests with Selenium. In my experience Selenium and Chromedriver are finicky to setup and 
as such benefit greatly from being containerized.
In addition, I wanted to be able to trigger these tests through http calls, which makes the whole system very easy to use.
And thus, docker-flask-selenium-chromedriver was born.

# How to use it?

The image comes with a docker-compose yml and as such you can simply start the image with the following command:

```console
cd 3.12-slim
docker compose up
```

By default, the web server will run on port 8000 and there's a /test endpoint that connects to [httpbin](https://httpbin.org/html) and returns OK if it was able to read the H1 tag.

e.g. you can confirm by running:

```console
curl 127.0.0.1:8000/test
OK
```

# Image build

The image is based on `python-slim` image, which itself is based on `debian:bookworm-slim`. It adds:

Installed from apt:
 - chromium
 - chromium-driver
 
Installed from pip through requirements.txt
 - flask
 - gunicorn
 - selenium
 
