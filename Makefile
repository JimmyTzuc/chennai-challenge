.PHONY: init

init: down up

down:
		docker compose down --volumes --remove-orphans

pull:
		docker compose pull

build:
		docker compose build

up: pull build
		docker compose up -d
