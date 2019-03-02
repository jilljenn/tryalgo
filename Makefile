help:
	@echo "make pycodestyle  run pycodestyle on Python source"
	@echo "make pylint       run pylint on Python source"

pycodestyle:
	-@find setup.py tryalgo -type f -name '*.py' | xargs pycodestyle

pylint:
	-@find setup.py tryalgo -type f -name '*.py' | xargs pylint -j 4

.PHONY: help pycodestyle pylint bin
