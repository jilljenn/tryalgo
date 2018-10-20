#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Left and right inversions in a table
# christoph durr - 2016-2018


# snip{
def _merge_sort(tab, tmp, rank, left, right, lo, hi):
    if hi <= lo + 1:             # interval is empty or singleton
        return                   # nothing to do
    mid = lo + (hi - lo) // 2    # divide interval into [lo:mid], [mid:hi]
    _merge_sort(tab, tmp, rank, left, right, lo, mid)
    _merge_sort(tab, tmp, rank, left, right, mid, hi)
    i = lo                       # merge both lists
    j = mid
    k = lo
    while k < hi:
        if i < mid and (j == hi or tab[rank[i]] <= tab[rank[j]]):
            tmp[k] = rank[i]
            right[rank[i]] += j - mid
            i += 1
        else:
            tmp[k] = rank[j]
            left[rank[j]] += mid - i
            j += 1
        k += 1
    for k in range(lo, hi):      # copy sorted segment into original table
        rank[k] = tmp[k]


def left_right_inversions(tab):
    """ Compute left and right inversions of each element of a table.

    :param tab: list with comparable elements
    :returns: lists left and right. left[j] = the number of i<j such that tab[i] > tab[j].
              right[i] = the number of i<j such that tab[i] > tab[j].
    :complexity: `O(n \log n)`
    """
    n = len(tab)
    left = [0] * n
    right = [0] * n
    tmp = [None] * n      # temporary table
    rank = list(range(n))
    _merge_sort(tab, tmp, rank, left, right, 0, n)
    return left, right
# snip}
