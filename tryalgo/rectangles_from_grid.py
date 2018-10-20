#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Largest area rectangle in a binary matrix
# plus grand rectangle monochromatique
# jill-jenn vie et christoph durr - 2014-2018

from tryalgo.rectangles_from_histogram import rectangles_from_histogram


# snip{
def rectangles_from_grid(P, black=1):
    """Largest area rectangle in a binary matrix

    :param P: matrix
    :param black: search for rectangles filled with value black
    :returns: area, left, top, right, bottom of optimal rectangle
             consisting of all (i,j) with
             left <= j < right and top <= i <= bottom
    :complexity: linear
    """
    rows = len(P)
    cols = len(P[0])
    t = [0] * cols
    best = None
    for i in range(rows):
        for j in range(cols):
            if P[i][j] == black:
                t[j] += 1
            else:
                t[j] = 0
        (area, left, height, right) = rectangles_from_histogram(t)
        alt = (area, left, i, right, i-height)
        if best is None or alt > best:
            best = alt
    return best
# snip}
