.PHONY: download test test_coverage format

test:
	poetry run python -m pytest DataStructures Algorithms

test-coverage:
	poetry run python -m pytest --cov=DataStructures,Algorithms --cov-report xml --cov-report term


format:|
	poetry run black Algorithms DataStructures
	npm run-script format

lint:|
	poetry run flake8 --ignore=E203,W503
	poetry run black Algorithms DataStructures --check