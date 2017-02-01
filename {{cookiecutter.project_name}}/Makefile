#!/bin/bash
# Yet to be implemented
PROJECT_NAME={{cookiecutter.project_name}}
VENV_PATH={{cookiecutter.project_venv}}


setup:
	${VENV_PATH}/bin/pip install pip --upgrade
	${VENV_PATH}/bin/pip install -e . --upgrade
	${VENV_PATH}/bin/pip install -e '.[testing]' --upgrade

test:
	${VENV_PATH}/bin/python -m pytest -q --disable-pytest-warnings -r pPfxE

revision:
	@read -p "What did you add? " MSG && \
	${VENV_PATH}/bin/alembic revision --autogenerate -m "$$MSG"

upgrade:
	${VENV_PATH}/bin/alembic upgrade head

downgrade:
	${VENV_PATH}/bin/alembic downgrade -1

run:
	${VENV_PATH}/bin/pserve development.ini
