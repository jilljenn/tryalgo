[![Build Status](https://travis-ci.org/jilljenn/tryalgo.svg?branch=master)](https://travis-ci.org/jilljenn/tryalgo)
[![PyPI](https://img.shields.io/pypi/v/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)
[![PyPI](https://img.shields.io/pypi/pyversions/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)

# tryalgo

Basic and advanced algorithms and data structures for preparing programming competitions (e.g. ACM-ICPC) and coding interviews.  
By Christoph Dürr and Jill-Jênn Vie.

## Install

    pip install tryalgo

## Documentation

- [Documentation](http://jilljenn.github.io/tryalgo/) of tryalgo 1.3
- [Blog tryalgo.org](http://tryalgo.org) in French and English

## Demo: [TryAlgo in Paris](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

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

## Test

We prepared many tests. They can be used to practice your programming skills!

python -m unittest

## Found a bug?

Please [drop an issue](https://github.com/jilljenn/tryalgo/issues).

## Authors

© 2016–2018, Christoph Dürr and Jill-Jênn Vie (vie@jill-jenn.net).  
Released under the MIT License.

## Contributors

Thanks!

- Louis Abraham
- Lilian Besson
- Stéphane Henriot
- Ryan Lahfa
- Olivier Marty
- Samuel Tardieu
