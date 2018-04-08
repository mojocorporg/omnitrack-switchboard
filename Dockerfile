FROM python:3
LABEL maintainer="uzair_y3k@live.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
