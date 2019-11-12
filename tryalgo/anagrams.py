#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Anagrams
christoph dürr - jill-jênn vie - 2013-2018
"""


# snip{
# pylint: disable=anomalous-backslash-in-string
def anagrams(w):                   # w is a list of strings
    """group a list of words into anagrams

    :param w: list of strings
    :returns: list of lists

    :complexity:
        :math:`O(n k log k)` in average, for n words of length at most k.
        :math:`O(n^2 k log k)` in worst case due to the usage of a dictionary.
    """
    w = list(set(w))               # use set() to remove duplicates
    d = {}                       
    for i in range(len(w)):        # group words according to the signature
        s = ''.join(sorted(w[i]))  # calculate the signature
        if s in d:
            d[s].append(i)         # append a word to an existing signature
        else:
            d[s] = [i]             # add a new signature and its first word
    # -- extract anagrams
    answer = []
    for s in d:
        if len(d[s]) > 1:          # ignore words without anagram
            answer.append([w[i] for i in d[s]])
    return answer
# snip}
