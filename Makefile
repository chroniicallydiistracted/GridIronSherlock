SHELL := /bin/bash

.PHONY: setup generate fmt lint type test e2e build migrate seed start

setup:
	python3 -m venv .venv || true
	. .venv/bin/activate && pip install -U pip wheel || true

generate:
	echo "noop"

fmt:
	echo "noop"

lint:
	echo "noop"

type:
	echo "noop"

test:
	echo "noop"

e2e:
	echo "noop"

build:
	echo "noop"

migrate:
	echo "noop"

seed:
	echo "noop"

start:
	echo "noop"
