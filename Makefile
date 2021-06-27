.PHONY: run test env

run:
	poetry run python -m py_skeleton

test:
	poetry run pytest --cov=py_skeleton tests

env:
	poetry install
	poetry run pre-commit install
