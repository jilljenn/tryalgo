#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
suffix array,
but only the O(n log^2(n)) implementation, which is enough for most programming contest problems

christoph dürr 2024
"""

def sort_class(s):
    """ sorts s and returns additional information

    :param s: string or list
    :returns p, c: p[j]=i if s[i] has rank j in sorted(s) and c[i] is rank of s[i] in sorted(set(s))
    :complexity: O(n log n) or better if sort makes use of specific values in s
    """
    S_index = [(x, i) for i, x in enumerate(s)]
    p = [i for x, i in sorted(S_index)]
    x2c = {x : i for i, x in enumerate(sorted(set(s)))}
    c = [x2c[x] for x in s]
    return p, c


def sort_cyclic_shifts(s):
    """ given a string s, sort lexicographically all cyclic shifts of s.

    The i-th cyclic shift of s is s[i:] + s[i:]
    :param s: string or list
    :returns L: such that L[j]=i if the i-th cyclic shift of s has rank j
    :complexity: O(n * log(n)^2)
    """
    p, c = sort_class(s)
    n = len(s)
    K = 1
    while K <= n:
        L = [(c[i], c[(i + K) % n]) for i in range(n)]
        p, c = sort_class(L)
        K <<= 1 
    return p

def suffix_array(s):
    """ given a string s, sort lexicographically suffixes of s
    :param s: string
    :returns: R with R[i] is j such that s[j:] has rank i
    :complexity: O(n log^2 n)
    """
    special = chr(0)
    assert special < min(s) 
    L = sort_cyclic_shifts(s + special)
    return L[1:]

if __name__ == "__main__":
    # tested at https://www.spoj.com/problems/SARRAY/
    import sys

    def readstr(): return sys.stdin.readline().rstrip()
    def readstrs(): return readstr().split()
    def readints(): return map(int, readstrs())

    for val in suffix_array(readstr()):
        print(val)
