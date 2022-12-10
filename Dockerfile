# Компактная версия, 43 мб
FROM python:3.10.1-slim-bullseye

# Don't buffer stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"

RUN apt-get update && \
    apt-get install -y sudo git curl && \
    #echo "${APP_USER} ALL = NOPASSWD: /usr/sbin/update-ca-certificates" > /etc/sudoers.d/express_bot && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

ENV APP_USER=appuser
RUN useradd --create-home $APP_USER

ENV USER_PATH=/home/$APP_USER/.local/bin
ENV PATH="$VENV_PATH:$USER_PATH:$PATH"

RUN mkdir -p /home/$APP_USER/app
WORKDIR /home/$APP_USER/app
USER $APP_USER

COPY requirements.txt .
COPY src ./src
RUN pip install --no-cache-dir -r ./requirements.txt
WORKDIR /home/$APP_USER/app/src
