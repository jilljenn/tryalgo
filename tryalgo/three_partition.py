#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# subsetsum
# jill-jenn vie et christoph durr - 2015-2018


# snip{
def three_partition(x):
    """partition a set of integers in 3 parts of same total value

    :param x: table of non negative values
    :returns: triplet of the integers encoding the sets, or None otherwise
    :complexity: :math:`O(2^{2n})`
    """
    f = [0] * (1 << len(x))
    for i in range(len(x)):
        for S in range(1 << i):
            f[S | (1 << i)] = f[S] + x[i]
    for A in range(1 << len(x)):
        for B in range(1 << len(x)):
            if A & B == 0 and f[A] == f[B] and 3 * f[A] == f[-1]:
                return (A, B, ((1 << len(x)) - 1) ^ A ^ B)
    return None
# snip}
