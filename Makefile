test:
	pytest $(file) --pep8 -v

default: test
