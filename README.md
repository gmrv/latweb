# LATWEB


## Полезные команды manage.py
```
showmigrations my_app
migrate my_app migration-name
migrate my_app zero

makemigrations
migrate --plan

sqlsequencereset main

dumpdata api --indent 2 
```

## Скачать/загрузить бд
```bash
docker exec -it lat_backend python manage.py dumpdata --app api > db.json

# Удалить кривые символы в конце файла полученного на предыдущем шаге
docker exec -it lat_backend python manage.py loaddata --app api db.json
```
