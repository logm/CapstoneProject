FROM python:latest

WORKDIR /project
# ADD project
ADD . /project

RUN pip install -r requirements.txt

# RUN export FLASK_ENV=development
ENV FLASK_RUN_HOST 0.0.0.0
# ENV FLASK_ENV=production
ENV FLASK_ENV=development
# RUN export FLASK_APP=microblog.py
ENV FLASK_APP microblog.py

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN apt-get update && apt-get install

# CMD flask run