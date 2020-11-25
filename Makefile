#!/bin/bash
.PHONY: default
.SILENT:


default:

shell:
	docker-compose stop api
	docker-compose run --rm --service-ports api bash

createsuperuserfast:
	docker-compose run --rm api python manage.py createsuperuserfast --email 'admin@email.com' --password cash1234 --noinput

createsuperuser:
	docker-compose run --rm api python manage.py createsuperuser

migrations:
	docker-compose run --rm api python manage.py makemigrations

migrate:
	docker-compose run --rm api python manage.py migrate --noinput

start:
	docker-compose up -d

start_api:
	docker-compose run --rm --service-ports api

stop:
	docker-compose down

collectstatic:
	docker-compose run --rm api python manage.py collectstatic --noinput

build:
	docker-compose build --force-rm --no-cache --pull
	make collectstatic
	make tests

setup:
	docker network create cashback_net
	docker-compose build --force-rm --no-cache --pull
	make migrations
	make migrate
	make collectstatic
	make createsuperuserfast
	make collectstatic
	make tests

logs:
	docker-compose logs --follow

tests:
	docker-compose run --rm api python manage.py test

clean:
	make stop
	docker image rm $$(docker image ls -q -f reference=cashback_django_api)
	docker volume rm $$(docker volume ls -q -f name=cashback)
	docker network rm cashback_net

startapp:
	docker-compose stop api
	docker-compose run --rm api python manage.py startapp $(app)
	mv -f $(app) cashback_api/
	touch cashback_api/$(app)/serializers.py
	touch cashback_api/$(app)/choices.py
	touch cashback_api/$(app)/routers.py
	touch cashback_api/$(app)/services.py
