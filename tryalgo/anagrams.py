#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Anagrams

# christoph dürr - jill-jênn vie - 2013 - 2015


# snip{
def anagrams(w):
    """group a list of words into anagrams

    :param w: list of strings
    :returns: list of lists

    :complexity:
        :math:`O(n k \log k)` in average, for n words of length at most k.
        :math:`O(n^2 k \log k)` in worst case due to the usage of a dictionary.
    """
    w = list(set(w))               # retirer les doublons
    d = {}                         # grouper les mots par même signature
    for i in range(len(w)):
        s = ''.join(sorted(w[i]))  # signature
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]
    # -- extraire anagrammes
    reponse = []
    for s in d:
        if len(d[s]) > 1:          # ignorer mots sans anagramme
            reponse.append([w[i] for i in d[s]])
    return reponse
# snip}
