#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Next permutation
prochaine permuation

jill-jênn vie et christoph dürr - 2014-2020
"""

from sys import argv
import sys
from tryalgo.our_std import readint, readstr


# snip{
# pylint: disable=redefined-outer-name
def next_permutation(tab):
    """find the next permutation of tab in the lexicographical order

    :param tab: table with n elements from an ordered set
    :modifies: table to next permutation
    :returns: False if permutation is already lexicographical maximal
    :complexity: O(n)
    """
    i = len(tab) - 2                    # find pivot
    while i >= 0 and tab[i] >= tab[i + 1]:
        i -= 1

    if i < 0:           # tab is already the last permutation
        return False

    j = len(tab) - 1                    # find element to swap
    while tab[j] <= tab[i]:
        j -= 1
    tab[i], tab[j] = tab[j], tab[i]     # swap
    tab[i + 1:] = reversed(tab[i + 1:]) # inverse suffix
    # n = len(tab)
    # pivot = None                         # find pivot
    # for i in range(n - 1):
    #     if tab[i] < tab[i + 1]:
    #         pivot = i
    # if pivot is None:                    # tab is already the last perm.
    #     return False
    # for i in range(pivot + 1, n):        # find the element to swap
    #     if tab[i] > tab[pivot]:
    #         swap = i
    # tab[swap], tab[pivot] = tab[pivot], tab[swap]
    # tab[swap + 1:] = reversed(tab[swap + 1:])    # invert suffix
    return True
# snip}

# icpc-ignore
# snip{ word_addition
# pylint: disable=redefined-outer-name
def convert(word, ass):
    """
    solves a cryptogram in the style SEND + MORE = MONEY
    """
    retval = 0
    for x in word:
        retval = 10 * retval + ass[x]
    return retval


# pylint: disable=redefined-outer-name
def solve_word_addition(S):         # returns number of solutions
    """returns number of solutions"""
    n = len(S)
    letters = sorted(list(set(''.join(S))))
    not_zero = ''                   # letters that cannot be 0
    for word in S:
        not_zero += word[0]
    tab = ['@'] * (10 - len(letters)) + letters  # minimal lex permutation
    count = 0
    while True:
        ass = {tab[i]: i for i in range(10)}  # dict = associative array
        if tab[0] not in not_zero:
            difference = -convert(S[n - 1], ass)  # do the addition
            for word in S[:n - 1]:
                difference += convert(word, ass)
            if difference == 0:                   # does it add up?
                count += 1
        if not next_permutation(tab):
            break
    return count
# snip}


if __name__ == "__main__":
    if len(argv) > 1:
        L = argv[1:]
        if len(L) == 1:
            L = list(L[0])
        while True:
            print(L)
            if not next_permutation(L):
                sys.exit(0)

    n = readint()
    S = [readstr() for _ in range(n)]
    print(solve_word_addition(S))
