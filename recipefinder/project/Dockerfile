# FROM python:3.6-alpine

# RUN adduser -D microblog

# WORKDIR /home/microblog

# COPY requirements.txt requirements.txt
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements.txt
# RUN venv/bin/pip install gunicorn

# COPY app app
# COPY migrations migrations
# COPY microblog.py config.py boot.sh ./
# RUN chmod +x boot.sh

# ENV FLASK_APP microblog.py

# RUN chown -R microblog:microblog ./
# USER microblog

# EXPOSE 5000
# ENTRYPOINT ["./boot.sh"]




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