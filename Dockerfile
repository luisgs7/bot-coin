FROM python:3.10.6-alpine3.16
LABEL maintainer="iadevlab.com"

ENV PYTHONUNBUFFERED 1

COPY ./data /data
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /data

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    adduser \
    --disabled-password \
    --no-create-home \
    homer-user

ENV PATH="/py/bin:$PATH"

USER homer-user