[![Build Status](https://travis-ci.org/jilljenn/tryalgo.svg?branch=master)](https://travis-ci.org/jilljenn/tryalgo)
[![PyPI](https://img.shields.io/pypi/v/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)

# tryalgo

Basic and advanced algorithms and data structures  
By Christoph Dürr and Jill-Jênn Vie.

## Install

[![PyPI](https://img.shields.io/pypi/pyversions/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)

    pip install tryalgo

## Additional information

- [Documentation](http://jilljenn.github.io/tryalgo/) on GitHub Pages
- [Blog tryalgo.org](http://tryalgo.org)

## Demo: [TryAlgo in Paris](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb"><img src="http://tryalgo.org/static/paris.png" /></a>

## Usage

**Dynamic programming** some example with coin change:

```python
from tryalgo import coin_change

print(coin_change([3, 5, 11], 29))  # True because 29 = 6*3 + 0*5 + 1*11
```

***Des chiffres et des lettres*** (that inspired *Countdown*)

```python
tryalgo.arithm_expr_target import arithm_expr_target

arithm_expr_target([25, 50, 75, 100, 3, 6], 952)
```

Returns `'((((75*3)*(100+6))-50)/25)=952'`.

## Found a bug?

Please [drop an issue](https://github.com/jilljenn/tryalgo/issues)!

## Authors

© Christoph Dürr and Jill-Jênn Vie (vie@jill-jenn.net).  
Released under the MIT License.

Contributors include:

- Louis Abraham
- Lilian Besson
- Stéphane Henriot
- Ryan Lahfa
- Olivier Marty
