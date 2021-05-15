ENV_NAME=cms-env
BIN=$(ENV_NAME)/bin/
PYTHON=$(BIN)/python
REQUIREMENTS=requirements.txt

create_environment:
	make clean
	$(PYTHON) -m venv $(ENV_NAME)

clean:
	rm -rf $(ENV_NAME)
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf flask_session/
	rm -f .coverage
	rm -rf tests/.pytest_cache
	rm -rf htmlcov

install_requirements:
	$(BIN)pip install -r $(REQUIREMENTS)

# Run unittests and generate html coverage report
test:
	coverage run -m pytest tests
	coverage html

# Run linters check only
lint:
	$(BIN)isort . --skip $(ENV_NAME) --check
	$(BIN)black . --exclude=$(ENV_NAME) --check

# Run linters and try to fix the errors
format:
	$(BIN)isort . --skip $(ENV_NAME)
	$(BIN)black . --exclude=$(ENV_NAME)

# Update all libraries required to run this application
requirements_txt:
	pip freeze > requirements.txt

# Re/install the virtual environment with all requirements
install:
	make install_requirements

# Do all checks.
build:
	make dev_install
	make lint
	make test
