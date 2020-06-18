.PHONY: build
build:	inc-build	## bump build and package project for PyPi
	python setup.py sdist bdist_wheel
	twine check dist/*

.PHONY: pypitest
pypitest:	## Upload project to PyPi test site
	twine upload  --repository testpypi dist/*

.PHONY: upload
upload:	## Upload new version to PyPi
	twine upload dist/*
