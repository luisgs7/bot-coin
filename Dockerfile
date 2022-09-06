FROM python:3.10.6-alpine3.16
LABEL maintainer="iadevlab.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    adduser \
    --disabled-password \
    --no-create-home \
    homer-user

ENV PATH="/py/bin:$PATH"

USER homer-user