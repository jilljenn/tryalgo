help::
	@echo "make pycodestyle  run pycodestyle on Python source"
	@echo "make pylint       run pylint on Python source"

tests::
	python -m unittest 

pycodestyle::
	-@find setup.py tryalgo -type f -name '*.py' | xargs pycodestyle

pylint::
	-@find setup.py tryalgo -type f -name '*.py' | xargs pylint --disable=C0103 -j 4

.PHONY: help pycodestyle pylint bin docs

docs::
	cd docs/_static && convert logo_W.png logo_B.png +append logo_white.png
	sphinx-apidoc -f -o docs/tryalgo tryalgo
	sphinx-build docs docs/_build
