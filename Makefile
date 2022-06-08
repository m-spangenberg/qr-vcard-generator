# Prepare the virtual environment and install dependencies
init:
    pip install pipenv
    pipenv sync

# Prepare the virtual environment and run pytest unittests
tested:
    pip install pipenv
    pipenv install --dev
	pipenv run pytest

# Prepare virtual environment and install developement dependencies
dev:
    pip install pipenv
    pipenv install --dev

# Check that Pipfile is up to date and generate new requirements.txt and dev-requirements.txt
prep:
	pipenv update
	pipenv lock --requirements
	pipenv lock --requirements --dev-only