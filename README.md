# yamdb_final
yamdb_final
### Описание
docker-compose к проекту [api_yamdb](https://github.com/marlooooo/api_yamdb)
### Технологии
- Python 3.7
- Django 2.2.19
- Django REST Framework
### CD/CI
[Проект можно посмотреть здесь](http://marlo.sytes.net)
[Документация проекта](http://marlo.sytes.net/redoc)
![workflow](https://github.com/marlooooo/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
### Запуск проекта в dev-режиме
- перейти в директорию infra и создать файл .env и оформить по такому образцу
```
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
```
- запустить docker-compose ```docker-compose up --build -d```
- выполнить миграции, собрать статику и создать суперпользователя
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
docker-compose exec web python manage.py createsuperuser
```
- перезапустить docker-compose
### Авторы
* [Агапов Владислав](https://github.com/marlooooo)
* [Анастасия Ничипорчук](https://github.com/AngryFennec)
* [Дмитрий Кутин](https://github.com/Tacostrophe)

