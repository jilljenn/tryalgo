#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Anagrams
christoph dürr - jill-jênn vie - 2013-2019
"""


# snip{
# pylint: disable=anomalous-backslash-in-string
def anagrams(S):                   # S is a set of strings
    """group a set of words into anagrams

    :param S: set of strings
    :returns: list of lists of strings

    :complexity:
        :math:`O(n k log k)` in average, for n words of length at most k.
        :math:`O(n^2 k log k)` in worst case due to the usage of a dictionary.
    """
    d = {}                         # maps s to list of words with signature s
    for word in S:                 # group words according to the signature
        s = ''.join(sorted(word))  # calculate the signature
        if s in d:
            d[s].append(word)      # append a word to an existing signature
        else:
            d[s] = [word]          # add a new signature and its first word
    # -- extract anagrams, ingoring anagram groups of size 1
    return [d[s] for s in d if len(d[s]) > 1]
# snip}
