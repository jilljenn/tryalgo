#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Interval tree
# christoph dürr - jill-jênn vie - 2013-2018

from bisect import bisect_right


# snip{
class _Node:
    def __init__(self, center, by_low, by_high, left, right):
        self.center = center
        self.by_low = by_low
        self.by_high = by_high
        self.left = left
        self.right = right


def interval_tree(intervals):
    """Construct an interval tree

    :param intervals: list of half-open intervals
                      encoded as value pairs [left, right)
    :assumes: intervals are lexicographically ordered
    :returns: the root of the interval tree
    :complexity: O(n log n)
    """
    # the following test would degrade performance
    # assert intervals == sorted(intervals)
    if intervals == []:
        return None
    center = intervals[len(intervals) // 2][0]
    L = []
    R = []
    C = []
    for I in intervals:
        if I[1] <= center:
            L.append(I)
        elif center < I[0]:
            R.append(I)
        else:
            C.append(I)
    by_low = sorted((I[0], I) for I in C)
    by_high = sorted((I[1], I) for I in C)
    IL = interval_tree(L)
    IR = interval_tree(R)
    return _Node(center, by_low, by_high, IL, IR)


def intervals_containing(t, p):
    """Query the interval tree

    :param t: root of the interval tree
    :param p: value
    :returns: a list of intervals containing p
    :complexity: O(log n + m), where n is the number of intervals in t,
                and m the length of the returned list
    """
    INF = float('inf')
    if t is None:
        return []
    if p < t.center:
        retval = intervals_containing(t.left, p)
        j = bisect_right(t.by_low, (p, (INF, INF)))
        for i in range(j):
            retval.append(t.by_low[i][1])
    else:
        retval = intervals_containing(t.right, p)
        i = bisect_right(t.by_high, (p, (INF, INF)))
        for j in range(i, len(t.by_high)):
            retval.append(t.by_high[j][1])
    return retval
# snip}
