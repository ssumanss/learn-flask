# pull official base image
FROM python:slim

## 
RUN apt update -y
RUN apt install -y build-essential libpq-dev
RUN pip install psycopg2-binary --no-binary psycopg2-binary

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/