# base image  
FROM python:3.9-alpine   
LABEL maintainer="cianograd@gmail.com"
# setup environment variable  
COPY ./requirements.txt /requirements.txt
COPY ./code /code
WORKDIR /code
RUN python -m venv /py && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"
USER django-user