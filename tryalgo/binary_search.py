#!/usr/bin/env pypy3
# Binary search
# jill-jenn vie et christoph durr - 2014-2015

from sys import stdin

__all__ = ["discrete_binary_search", "continuous_binary_search",
           "optimized_binary_search_lower", "optimized_binary_search"]

# Fill the Cisterns
# http://www.spoj.com/problems/CISTFILL/
# [!] python3 est trop lent pour ce problème


def readint():
    return int(stdin.readline())


def readarray(f):
    return tuple(map(f, stdin.readline().split()))


# snip{ discrete_binary_search
def discrete_binary_search(tab, lo, hi):
    """Binary search in a table

    :param tab: boolean monotone table with tab[hi] = True
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
def continuous_binary_search(f, lo, hi):
    """Binary search for a function

    :param f: boolean monotone function with f(hi) = True
    :returns: first value x in [lo,hi] such that f(x),
             x is computed up to some precision
    :complexity: `O(log(hi-lo))`
    """
    while hi - lo > 1e-4:     # régler la précision voulue ici
        mid = (lo + hi) / 2.  # division flottante
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


if __name__ == "__main__":
    def volume(level):
        vol = 0
        for base, height, ground in rect:
            if base<level:
                vol += ground * min(level-base, height)
        return vol

    for test in range(readint()):
        n = readint()
        rect = []
        for _ in range(n):
            t = stdin.readline().split()
            rect.append( (int(t[0]), int(t[1]), int(t[2]) * int(t[3])) )
        V = readint()
        hi = 1e6 + 40000
        if volume(hi) < V:
            print("OVERFLOW")
        else:
            print("%.02f" % \
                  continuous_binary_search(lambda x: volume(x)>=V, 0, hi))
