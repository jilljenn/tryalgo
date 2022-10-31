#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Pareto sets

jill-jenn vie et christoph durr - 2022
"""
from tryalgo.fenwick import FenwickMin

def pareto2d(points):
    """ Compute the Pareto set of a given set of points in 2 dimensions

    :param points: list of tuples with the coordinates of the points. Can be floating point coordinates.
    :modifies: points will be sorted
    :returns: a list of non-dominated points
    :complexity: $O(n\\log n)$
    """
    pareto = []
    points.sort()
    for p in points:
        x, y = p
        if pareto == [] or y < pareto[-1][1] or p == pareto[-1]: 
            pareto.append(p)
    return pareto


def pareto3d(points):
    """ Compute the Pareto set of a given set of points in 2 dimensions

    :param points: list of tuples with the coordinates of the points. Can be floating point coordinates.
    :modifies: points will be sorted
    :returns: a list of non-dominated points
    :complexity: $O(n\\log n)$
    """
    # compute the ranks, it is ok to have multple y-values in the list
    y_values = [y for x,y,z in points]
    y_values.sort()
    rank = {}
    for i, yi in enumerate(y_values):
        rank[yi] = i
    n = len(points)
    points.sort()    # sort by rank in first competition
    pareto = []
    R = FenwickMin(n)
    for p in points:
        x, y, z = p 
        i = rank[y]
        if pareto == [] or R.prefixMin(i) > z or p == pareto[-1]:
            pareto.append(p) 
        R.update(i, z)
    return pareto 
