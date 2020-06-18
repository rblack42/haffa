.PHONY: run
run:    ## Run project application
	python3 -m $(PROJECT)

.PHONY: pyinit
pyinit:	## Create Python virtual environment
	test -d _venv || \
	python3 -m venv _venv && \
	source _venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -e .

.PHONY: pyreqs
pyreqs: requirements.txt 	## Load Python requirements
	source _venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	tox -v

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

.PHONY: deploy
deploy:	## deploy web pages to public server
	scripts/deploy.sh

.PHONY: type-check
type-check:	## Check types with mypy
	mypy sphinxcontrib
