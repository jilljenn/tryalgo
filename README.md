[![PyPI](https://img.shields.io/pypi/v/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)
[![PyPI](https://img.shields.io/pypi/pyversions/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)
![Pylint score](https://mperlet.github.io/pybadge/badges/10.svg)
[![Codecov](https://img.shields.io/codecov/c/github/jilljenn/tryalgo.svg)](https://codecov.io/gh/jilljenn/tryalgo/)

# Algorithmic Problem Solving

Algorithms and data structures for preparing programming competitions (e.g. ICPC, [see more](https://tryalgo.org/contests/)) and coding interviews.  
By Christoph Dürr and Jill-Jênn Vie.

[Our book](https://tryalgo.org/book) is available in French, English, Simplified and Traditional Chinese.

## Install

    pip install tryalgo

## Documentation

- [Documentation](http://jilljenn.github.io/tryalgo/) of tryalgo 1.4
- [Blog tryalgo.org](http://tryalgo.org) in French and English

## Demo: [TryAlgo in Paris](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

Shortest paths on the graph of Paris.

To run it yourself:

    pip install -r examples/requirements.txt
	jupyter notebook  # Then go to examples folder

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb"><img src="http://tryalgo.org/static/paris.png" /></a>

## Usage

**Dynamic programming** some example with coin change:

```python
from tryalgo import coin_change

print(coin_change([3, 5, 11], 29))  # True because 29 = 6 x 3 + 0 x 5 + 1 x 11
```

***Des chiffres et des lettres*** (that inspired *Countdown*)

```python
from tryalgo.arithm_expr_target import arithm_expr_target

arithm_expr_target([25, 50, 75, 100, 3, 6], 952)
```

Returns `'((((75*3)*(100+6))-50)/25)=952'`.

## Tests

All algorithms are thoroughly tested. These tests can be used to [practice your programming skills](https://tryalgo.org/en/miscellaneous/2019/08/10/how-to-practice-algorithms-with-tryalgo/)!

```python
python -m unittest
```

Most snippets from the book are within 76 columns (French version) or 75 columns (English version).

Our code is checked. Using optional requirements, you can check it too:

    pip install pycodestyle pylint
    make pycodestyle  # PEP8
	make pylint

## Found a bug?

Please [drop an issue](https://github.com/jilljenn/tryalgo/issues).

## Authors

© 2016–2023, Christoph Dürr and Jill-Jênn Vie (vie@jill-jenn.net).  
Released under the MIT License.

## Contributors

Thanks!

- Louis Abraham
- Lilian Besson
- Xavier Carcelle
- Stéphane Henriot
- Ryan Lahfa
- Olivier Marty
- Samuel Tardieu
