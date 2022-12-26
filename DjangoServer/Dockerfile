FROM python:3.9

WORKDIR /usr/src/app

COPY . .
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

RUN pip install tweepy
RUN pip install mysqlclient
RUN pip install -U pip wheel cmake

RUN pip install -r requirements.txt
CMD ["bin/sh", "-c", "python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000