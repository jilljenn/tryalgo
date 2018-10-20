#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Union of intervals
# jill-jenn vie et christoph durr - 2014-2018


# snip{
def intervals_union(S):
    """Union of intervals

    :param S: list of pairs (low, high) defining intervals [low, high)
    :returns: ordered list of disjoint intervals with the same union as S
    :complexity: O(n log n)
    """
    E = [(low, -1) for (low, high) in S]
    E += [(high, +1) for (low, high) in S]
    nb_open = 0
    last = None
    retval = []
    for x, _dir in sorted(E):
        if _dir == -1:
            if nb_open == 0:
                last = x
            nb_open += 1
        else:
            nb_open -= 1
            if nb_open == 0:
                retval.append((last, x))
    return retval
# snip}
