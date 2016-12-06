[![Build Status](https://travis-ci.org/jilljenn/tryalgo.svg?branch=master)](https://travis-ci.org/jilljenn/tryalgo)
[![PyPI](https://img.shields.io/pypi/v/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)
[![PyPI](https://img.shields.io/pypi/dm/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)
[![PyPI](https://img.shields.io/pypi/pyversions/tryalgo.svg)](https://pypi.python.org/pypi/tryalgo/)

# tryalgo

Basic and advanced algorithms and data structures
By Christoph Dürr and Jill-Jênn Vie.

## Install

    pip3 install tryalgo

## Additional information

- http://pythonhosted.org/tryalgo/
- http://tryalgo.org

## Demo: [TryAlgo in Paris](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb"><img src="http://tryalgo.org/static/paris.png" /></a>

## Usage

**Dynamic programming** some example with coin change:

```python
from tryalgo.subsetsum import coin_change

print(coin_change([3, 5, 11], 29))  # True because 29 = 6*3 + 0*5 + 1*11
```

## Found a bug?

Please [drop an issue](https://github.com/jilljenn/tryalgo/issues)!

## Authors

© Christoph Dürr and Jill-Jênn Vie (vie@jill-jenn.net). Released under the MIT License.

Contributors include:

- Louis Abraham
- Ryan Lahfa
