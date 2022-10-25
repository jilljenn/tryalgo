#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
"""\
Binary search

jill-jênn vie, christoph dürr et louis abraham - 2014-2020
"""

# pylint: disable=redefined-outer-name

from tryalgo.our_std import readint, readarray

__all__ = ["discrete_binary_search", "continuous_binary_search",
           "optimized_binary_search_lower", "optimized_binary_search",
           "ternary_search"]

# Fill the Cisterns
# http://www.spoj.com/problems/CISTFILL/
# [!] python3 is too slow for this problem

# snip{ discrete_binary_search


def discrete_binary_search(tab, lo, hi):
    """Binary search in a table

    :param tab: boolean monotone table with tab[hi] = True
    :param int lo:
    :param int hi: with hi >= lo
    :returns: first index i in [lo,hi] such that tab[i]
    :complexity: `O(log(hi-lo))`
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if tab[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
# snip}


# snip{ continuous_binary_search
def continuous_binary_search(f, lo, hi, gap=1e-4):
    """Binary search for a function

    :param f: boolean monotone function with f(hi) = True
    :param int lo:
    :param int hi: with hi >= lo
    :param float gap:
    :returns: first value x in [lo,hi] such that f(x),
             x is computed up to some precision
    :complexity: `O(log((hi-lo)/gap))`
    """
    while hi - lo > gap:
        mid = (lo + hi) / 2.0
        if f(mid):
            hi = mid
        else:
            lo = mid
    return lo
# snip}


def optimized_binary_search_lower(tab, logsize):
    """Binary search in a table using bit operations

    :param tab: boolean monotone table
       of size :math:`2^\\textrm{logsize}`
       with tab[0] = False
    :param int logsize:
    :returns: last i such that not tab[i]
    :complexity: O(logsize)
    """
    lo = 0
    intervalsize = (1 << logsize) >> 1
    while intervalsize > 0:
        if not tab[lo | intervalsize]:
            lo |= intervalsize
        intervalsize >>= 1
    return lo


# snip{ optimized_binary_search
def optimized_binary_search(tab, logsize):
    """Binary search in a table using bit operations

    :param tab: boolean monotone table
       of size :math:`2^\\textrm{logsize}`
       with tab[hi] = True
    :param int logsize:
    :returns: first i such that tab[i]
    :complexity: O(logsize)
    """
    hi = (1 << logsize) - 1
    intervalsize = (1 << logsize) >> 1
    while intervalsize > 0:
        if tab[hi ^ intervalsize]:
            hi ^= intervalsize
        intervalsize >>= 1
    return hi
# snip}


def ternary_search(f, lo, hi, gap=1e-10):
    """Ternary maximum search for a bitonic function

    :param f: boolean bitonic function (increasing then decreasing, not necessarily strictly)
    :param int lo:
    :param int hi: with hi >= lo
    :param float gap:
    :returns: value x in [lo,hi] maximizing f(x),
             x is computed up to some precision
    :complexity: `O(log((hi-lo)/gap))`
    """
    while hi - lo > gap:
        step = (hi - lo) / 3.
        if f(lo + step) < f(lo + 2 * step):
            lo += step
        else:
            hi -= step
    return lo


# pylint: disable=cell-var-from-loop
if __name__ == "__main__":
    def volume(level):
        """
        Computes the volume of a set of cuboids.
        """
        vol = 0
        for base, height, ground in rect:
            if base < level:
                vol += ground * min(level - base, height)
        return vol

    for test in range(readint()):
        n = readint()
        rect = []
        for _ in range(n):
            x, y, w, h = readarray(int)
            rect.append((x, y, w * h))
        V = readint()
        hi = 1e6 + 40000
        if volume(hi) < V:
            print("OVERFLOW")
        else:
            print("%.02f" %
                  continuous_binary_search(lambda x: volume(x) >= V,
                                           0, hi))
