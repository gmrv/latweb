# Django Template Project


## Конфигурация

Параметры конфигурации расположены в файле `src/.env`, например, смотри файл `src/.env.dist`.

## Установка на машине разработчика

Порядок установки:
```
pip install -r requirements.txt
cd src
cp .env.dist .env  # default environment variables
```

После установки: 
```
python3 ./manage.py migrate
python3 ./manage.py createsuperuser
```

## Установка на машине разработчика (Docker)
```
docker-compose up -d
```
после этого необходимо подключиться к контейнеру <имя_проекта>_backend_1 и выполнить:
```
python3 ./manage.py migrate
python3 ./manage.py createsuperuser
```


## Полезные команды manage.py
```
showmigrations my_app - показать все записи (из таблицы django_migrations)
migrate my_app migration-name - откатиться на указанную миграцию
migrate my_app zero - откатить все миграции

makemigrations - создать миграции
migrate --plan - показать план миграции

Чтоб сбрость все ключи в приложении (main) выполнить:
sqlsequencereset main
```