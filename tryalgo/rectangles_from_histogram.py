#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Largest Rectangular Area in a Histogram
# jill-jenn vie et christoph durr - 2014-2018


# snip{
def rectangles_from_histogram(H):
    """Largest Rectangular Area in a Histogram

    :param H: histogram table
    :returns: area, left, height, right, rect. is [0, height] * [left, right)
    :complexity: linear
    """
    best = (float('-inf'), 0, 0, 0)
    S = []
    H2 = H + [float('-inf')]  # extra element to empty the queue
    for right in range(len(H2)):
        x = H2[right]
        left = right
        while len(S) > 0 and S[-1][1] >= x:
            left, height = S.pop()
            # first element is area of candidate
            rect = (height * (right - left), left, height, right)
            if rect > best:
                best = rect
        S.append((left, x))
    return best
# snip}
