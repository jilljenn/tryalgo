#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Majority

jill-jenn vie et christoph durr - 2014-2019
"""


# snip{
# pylint: disable=unused-variable
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
    assert L    # majority is undefined on the empty set
    # snip{
    count = {}
    for word in L:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # Using min() like this gives the first word with
    #   maximal count "for free"
    val_1st_max, arg_1st_max = min((-count[word], word) for word in count)
    return arg_1st_max
# snip}
