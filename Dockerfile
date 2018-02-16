FROM python:3
LABEL maintainer="uzair_y3k@live.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
ADD . /code/
