#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# trie - correcteur orthographique
# jill-jenn vie et christoph durr - 2014-2018

# Don't write a Trie class otherwise you cannot represent leaves with None

# snip{
from string import ascii_letters    # in Python 2 one would import letters


class Trie_Node:
    def __init__(self):
        self.isWord = False
        self.s = {c: None for c in ascii_letters}


def add(T, w, i=0):
    """
    :param T: trie
    :param string w: word to be added to T
    :returns: new trie consisting of w added into T
    :complexity: O(len(w))
    """
    if T is None:
        T = Trie_Node()
    if i == len(w):
        T.isWord = True
    else:
        T.s[w[i]] = add(T.s[w[i]], w, i + 1)
    return T


def Trie(S):
    """
    :param S: set of words
    :returns: trie containing all words from S
    :complexity: linear in total word sizes from S
    """
    T = None
    for w in S:
        T = add(T, w)
    return T


def spell_check(T, w):
    """Spellchecker

    :param T: trie encoding the dictionary
    :param w: given word
    :returns: a closest word from the dictionary
    :complexity: linear if distance was constant
    """
    assert T is not None
    dist = 0
    while True:   # Try increasing distances
        u = search(T, dist, w)
        if u is not None:
            return u
        dist += 1


def search(T, dist, w, i=0):
    """Searches for w[i:] in trie T with distance at most dist
    """
    if i == len(w):
        if T is not None and T.isWord and dist == 0:
            return ""
        else:
            return None
    if T is None:
        return None
    f = search(T.s[w[i]], dist, w, i + 1)       # matching
    if f is not None:
        return w[i] + f
    if dist == 0:
        return None
    for c in ascii_letters:
        f = search(T.s[c], dist - 1, w, i)      # insertion
        if f is not None:
            return c + f
        f = search(T.s[c], dist - 1, w, i + 1)  # substitution
        if f is not None:
            return c + f
    return search(T, dist - 1, w, i + 1)        # deletion
# snip}
