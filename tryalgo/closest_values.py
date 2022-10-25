#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Closest values

jill-jênn vie et christoph dürr - 2014-2019
"""


# snip{
# pylint: disable=unused-variable
def closest_values(L):
    """Closest values

    :param L: list of values
    :returns: two values from L with minimal distance
    :modifies: the order of L
    :complexity: O(n log n), for n=len(L)
    """
    assert len(L) >= 2
    L.sort()
    valmin, argmin = min((L[i] - L[i - 1], i) for i in range(1, len(L)))
    return L[argmin - 1], L[argmin]
# snip}
