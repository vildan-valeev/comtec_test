# Тестовове задание
## ООО Комтек

[Условия][/docs/test_comtec.md] 


## Development
```sh
$ docker-compose up --build
```
Данные для тестов генерируются не из команды, а из фикстур автоматом, юзера создавать не нужно.
Для сброса данных необходимо использовать кастомную `./manage.py delete_data` и `./manage.py init_data`
Либо воспользоваться стандартными (flush, createsuperuser ...)

http://127.0.0.1:8000 - Admin Site
http://127.0.0.1:8000/api/swagger/ - Api Doc

login - admin
password - 25658545

## Other
### Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> <command>
```
### Database dump/load
```sh
$ python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --indent 4 > default_data.json

$ python manage.py loaddata default_data.json
```

## TODO:
1. 
