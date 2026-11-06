#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Merge two ordered lists

jill-jênn vie et christoph dürr - 2014-2019
"""


# snip{
def merge(x, y):
    """Merge two ordered lists
    Only to illustrate the technique, as this
    particular problem is solved by list(heap_merge(x, y)).

    :param x:
    :param y: x, y are non-decreasing ordered lists
    :returns: union of x and y in order
    :complexity: linear
    """
    z = []
    i = 0
    j = 0
    while i < len(x) or j < len(y):
        if j == len(y) or i < len(x) and x[i] <= y[j]:  # priority on x
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])                              # now switch to y
            j += 1
    return z
# snip}
