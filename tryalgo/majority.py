#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Majority
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def majority(L):
    # snip}
    """Majority

    :param L: list of elements
    :returns: element that appears most in L,
             tie breaking with smallest element
    :complexity: :math:`O(nk)` in average,
                 where n = len(L) and k = max(w for w in L)
                 :math:`O(n^2k)` in worst case due to the use of a dictionary
    """
    assert L    # majorité n'est pas définie sur ensemble vide
    # snip{
    compte = {}
    for mot in L:
        if mot in compte:
            compte[mot] += 1
        else:
            compte[mot] = 1
    valmin, argmin = min((-compte[mot], mot) for mot in compte)
    return argmin
# snip}

