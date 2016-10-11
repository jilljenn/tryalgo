#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Predictive text for mobile phones
# jill-jenn vie et christoph durr and louis abraham - 2014-2015

__all__ = ["predictive_text", "propose"]

# snip{
t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz   correspondance


def lettre_chiffre(x):
    """:returns: the digit correspondence for letter x"""
    assert 'a' <= x <= 'z'
    return t9[ord(x)-ord('a')]


def mot_code(mot):
    """:returns: the digit correspondence for word mot"""
    return ''.join(map(lettre_chiffre, mot))


def predictive_text(dico):
    """Predictive text for mobile phones

    :param dico: associates weights to words from [a-z]*
    :returns: a dictionary associating to words from [2-9]*
             a corresponding word from the dictionary with highest weight
    :complexity: linear in total word length
    """
    freq = {}   # freq[p] = poids total des mots de préfixe p
    for mot, poids in dico:
        prefixe = ""
        for x in mot:
            prefixe += x
            if prefixe in freq:
                freq[prefixe] += poids
            else:
                freq[prefixe] = poids
    #   prop[s] = préfixe à afficher sur s
    prop = {}
    for prefixe in freq:
        code = mot_code(prefixe)
        if code not in prop or freq[prop[code]] < freq[prefixe]:
            prop[code] = prefixe
    return prop


def propose(prop, seq):
    """wrapper to access a dictionary even for non present keys"""
    if seq in prop:
        return prop[seq]
    else:
        return "None"
# snip}
