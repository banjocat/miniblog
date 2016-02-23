FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DOCKER 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/code
RUN pip install -r requirements.txt
ADD . /code/
