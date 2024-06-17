# Variables
PYTHON := python
PIP := pip

# Targets
.PHONY: install
install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: lint
lint:
	flake8 .

.PHONY: test
test:
	pytest

.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: deploy
deploy: build up
