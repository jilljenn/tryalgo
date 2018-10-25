#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Predictive text for mobile phones
# jill-jenn vie et christoph durr and louis abraham - 2014-2018

__all__ = ["predictive_text", "propose"]

# snip{
t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz   mapping on the phone


def letter_to_digit(x):
    """:returns: the digit correspondence for letter x"""
    assert 'a' <= x <= 'z'
    return t9[ord(x) - ord('a')]


def code_word(word):
    """:returns: the digit correspondence for given word"""
    return ''.join(map(letter_to_digit, word))


def predictive_text(dic):
    """Predictive text for mobile phones

    :param dic: associates weights to words from [a-z]*
    :returns: a dictionary associating to words from [2-9]*
             a corresponding word from the dictionary with highest weight
    :complexity: linear in total word length
    """
    freq = {}   # freq[p] = total weight of words having prefix p
    for word, weight in dic:
        prefix = ""
        for x in word:
            prefix += x
            if prefix in freq:
                freq[prefix] += weight
            else:
                freq[prefix] = weight
    #   prop[s] = prefix to display for s
    prop = {}
    for prefix in freq:
        code = code_word(prefix)
        if code not in prop or freq[prop[code]] < freq[prefix]:
            prop[code] = prefix
    return prop


def propose(prop, seq):
    """wrapper to access a dictionary even for non-present keys"""
    if seq in prop:
        return prop[seq]
    else:
        return None
# snip}
