#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Next permutation
# prochaine permuation
# jill-jenn vie et christoph durr - 2014-2018

from sys import stdin, argv


# snip{
def next_permutation(tab):
    """find the next permutation of tab in the lexicographical order

    :param tab: table with n elements from an ordered set
    :modifies: table to next permutation
    :returns: False if permutation is already lexicographical maximal
    :complexity: O(n)
    """
    n = len(tab)
    pivot = None                         # find pivot
    for i in range(n - 1):
        if tab[i] < tab[i + 1]:
            pivot = i
    if pivot is None:                    # tab is already the last perm.
        return False
    for i in range(pivot + 1, n):        # find the element to swap
        if tab[i] > tab[pivot]:
            swap = i
    tab[swap], tab[pivot] = tab[pivot], tab[swap]
    i = pivot + 1
    j = n - 1                            # invert suffix
    while i < j:
        tab[i], tab[j] = tab[j], tab[i]
        i += 1
        j -= 1
    return True
# snip}


# solves a cryptogram in the style SEND + MORE = MONEY
# snip{ word_addition
def convert(word, ass):
    retval = 0
    for x in word:
        retval = 10 * retval + ass[x]
    return retval


def solve_word_addition(S):         # returns number of solutions
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
                exit(0)

    def _readstr():
        return stdin.readline().strip()

    def _readint():
        return int(stdin.readline())

    n = _readint()
    S = [_readstr() for _ in range(n)]
    print(solve_word_addition(S))
