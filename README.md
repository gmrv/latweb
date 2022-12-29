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

## Json Query JQ
```bash
jq . db.json | tail -n 1000 > db-last.json
```

## Agent
```bash
#!/bin/bash

cmdstr=$(curl -s -X POST http://localhost:8000/api/v1/livenessreport/test | jq -r '.post.command')

if [ "$cmdstr" == "null" ];
then
  echo "NULL";
else
  eval "${cmdstr}";
fi
```
