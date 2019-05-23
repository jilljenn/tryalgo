help:
	@echo "make pycodestyle  run pycodestyle on Python source"
	@echo "make pylint       run pylint on Python source"

test:
	@python3 tests/test_tryalgo.py

pycodestyle:
	-@find setup.py tryalgo -type f -name '*.py' | xargs pycodestyle

pylint:
	-@find setup.py tryalgo -type f -name '*.py' | xargs pylint --disable=C0103 -j 4

.PHONY: help pycodestyle pylint bin
