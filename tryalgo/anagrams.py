#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Anagrams
christoph dürr - jill-jênn vie - 2013-2019
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
    for i, word in enumerate(w):   # group words according to the signature
        s = ''.join(sorted(word))  # calculate the signature
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
