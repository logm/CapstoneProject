FROM python:2.7

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt
RUN export FLASK_APP=microblog.py
# EXPOSE 5000

RUN apt-get update && apt-get install

# CMD python app.py