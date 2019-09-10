#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Permute vector to minimize scalar product
jill-jenn vie et christoph durr - 2014-2018
"""


# snip{
def min_scalar_prod(x, y):
    """Permute vector to minimize scalar product

    :param x:
    :param y: x, y are vectors of same size
    :returns: min sum x[i] * y[sigma[i]] over all permutations sigma
    :complexity: O(n log n)
    """
    x1 = sorted(x)  # make copies to preserve
    y1 = sorted(y)  #    the  input arguments
    return sum(x1[i] * y1[-i - 1] for i in range(len(x1)))
# snip}
