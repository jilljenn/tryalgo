#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
How many rectangles can be formed from a set of points

jill-jenn vie et christoph durr - 2014-2018
"""


# snip{
def rectangles_from_points(S):
    """How many rectangles can be formed from a set of points

    :param S: list of points, as coordinate pairs
    :returns: the number of rectangles
    :complexity: :math:`O(n^2)`
    """
    answ = 0
    pairs = {}
    for j, _ in enumerate(S):
        for i in range(j):      # loop over point pairs (p,q)
            px, py = S[i]
            qx, qy = S[j]
            center = (px + qx, py + qy)
            dist = (px - qx) ** 2 + (py - qy) ** 2
            signature = (center, dist)
            if signature in pairs:
                answ += len(pairs[signature])
                pairs[signature].append((i, j))
            else:
                pairs[signature] = [(i, j)]
    return answ
# snip}
