#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Longest palindrome in a string by Manacher
# jill-jenn vie et christoph durr - 2014-2018

# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

# Algorithme de Manacher
# problème: plus long palindrome
# entrée: chaîne s
# sortie: indices i, j tel que s[i:j] est un palindrome
#         et que j-i est maximal et i maximal
# complexité: temps linéaire

# tous les indices réfèrent à une chaîne fictive t
# de la forme "^#a#b#a#a#$" si s="abaa"
# invariant: pour chaque préfixe vu
# on maintient un palindrome centré en c et de bord droit r
# qui maximise r
# ainsi que p[i] = plus grand rayon d'un palindrome centré en i


# snip{
def manacher(s):
    """Longest palindrome in a string by Manacher

    :param s: string
    :requires: s is not empty
    :returns: i,j such that s[i:j] is the longest palindrome in s
    :complexity: O(len(s))
    """
    assert set.isdisjoint({'$', '^', '#'}, s)  # Forbidden letters
    if s == "":
        return (0, 1)
    t = "^#" + "#".join(s) + "#$"
    c = 1
    d = 1
    p = [0] * len(t)
    for i in range(2, len(t) - 1):
        #                        -- reflect index i with respect to c
        mirror = 2 * c - i         # = c - (i-c)
        p[i] = max(0, min(d - i, p[mirror]))
        #                        -- grow palindrome centered in i
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        #                        -- adjust center if necessary
        if i + p[i] > d:
            c = i
            d = i + p[i]
    (k, i) = max((p[i], i) for i in range(1, len(t) - 1))
    return ((i - k) // 2, (i + k) // 2)  # extract solution
# snip}
