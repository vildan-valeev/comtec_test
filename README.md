# Тестовове задание
## ООО Комтек

[Условия тут](https://github.com/vildan-valeev/comtec_test/blob/master/docs/test_comtec.md)


## Development
```sh
запуск
$ docker-compose up --build
загрузка данных
$ docker exec -it app poetry run python manage.py loaddata default_data.json 
```
Данные для тестов генерируются из фикстур автоматом, юзера создавать не нужно.
Для сброса данных необходимо использовать кастомную команду `./manage.py delete_data` и `./manage.py init_data` - юзер не удаляется, только записи трех моделей
Либо воспользоваться стандартными (flush, createsuperuser ...)

http://0.0.0.0:8000 - Admin Site <br>
http://0.0.0.0:8000/api/swagger/ - Api Swagger Doc 

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
1. добавить django-split-settings - разделить settings на файлы, добавить файл с локальными настройками, переключение бд и тд,
2. вынести команды, тест в Makefile. Настройки, запуск в файлы *.sh
3. Настройка статики, если нужно
4. добавить гуникрн
5. добавить Postgres в docker-compose
