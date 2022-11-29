# Компактная версия, 43 мб
FROM python:3.10.1-slim-bullseye

# Don't buffer stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"

COPY requirements.txt /
COPY src /src
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /src
