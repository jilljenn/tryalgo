#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Permutate vector to minimize scalar product
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def min_scalar_prod(x, y):
    """Permute vector to minimize scalar product

    :param x:
    :param y: x,y are vectors of same size
    :returns: min sum x[i] * y[sigma[i]] over all permutations sigma
    :complexity: O(n log n)
    """
    x = sorted(x)  # faire des copies
    y = sorted(y)  # pour préserver les arguments
    return sum(x[i] * y[-i - 1] for i in range(len(x)))
# snip}
