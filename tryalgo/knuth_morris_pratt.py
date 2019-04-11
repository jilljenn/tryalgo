#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Find a substring by Knuth-Morris-Pratt
# jill-jênn vie et christoph dürr - 2014-2018
# inspired by a code from David Eppstein


# snip{
def knuth_morris_pratt(s, t):
    """Find a substring by Knuth-Morris-Pratt

    :param s: the haystack string
    :param t: the needle string
    :returns: index i such that s[i: i + len(t)] == t, or -1
    :complexity: O(len(s) + len(t))
    """
    assert t != ''          # does not work for empty string
    len_s = len(s)
    len_t = len(t)
    L = [0] * len_t         # compute array L
    j = L[0] = -1           # L[0] is the base case
    for i in range(1, len_t):  # compute L[i]
        while j >= 0 and t[i - 1] != t[j]:
            j = L[j]        # by finding best aligment
        j += 1              # we know: t[:j] == t[i-j:i]
        L[i] = j
    #                       - start actual search of t in s
    j = 0                   # j ranges in t
    k = 0                   # k ranges in s
    while k < len_s:
        while j >= 0 and s[k] != t[j]:  # find next poss. alignment
            j = L[j]
        j += 1
        k += 1              # we know: t[:j] == s[k-j:k]
        if j == len_t:      # we reached end of t
            return k - j    # hence found first occurence of t in s
    return -1               # we reached end of s, hence search failed
# snip}
