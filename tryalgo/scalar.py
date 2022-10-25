#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Permute vector to minimize scalar product

jill-jênn vie et christoph dürr - 2014-2019
"""


# snip{
def min_scalar_prod(x, y):
    """Permute vector to minimize scalar product

    :param x:
    :param y: x, y are vectors of same size
    :returns: min sum x[i] * y[sigma[i]] over all permutations sigma
    :complexity: O(n log n)
    """
    x1 = sorted(x)  # make copies to preserve the input arguments
    y1 = sorted(y)
    return sum(x1[i] * y1[-i - 1] for i in range(len(x1)))
# snip}
