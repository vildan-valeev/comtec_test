# Settings backend
Template for quick start project with Docker, Django, Dramatiq, Caddy, Gunicorn



## local
```sh
$ docker run --name redis -p 6379:6379 -d redis
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
$ python manage.py rundramatiq
```

## dev
```sh
$ docker-compose -f docker-compose.dev.yml up -d --build
```

## prod
```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```

## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> <command>
```
## Database dump/load
```sh
$ python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --indent 4 > default_data.json

$ python manage.py loaddata default_data.json
```
