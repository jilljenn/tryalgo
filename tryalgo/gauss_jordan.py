#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Linear equation system Ax=b by Gauss-Jordan
# jill-jenn vie et christoph durr - 2014-2018

__all__ = ["gauss_jordan", "GJ_ZERO_SOLUTIONS", "GJ_SINGLE_SOLUTION",
           "GJ_SEVERAL_SOLUTIONS"]


# snip{
def is_zero(x):                    # tolerance
    """error tolerant zero test
    """
    return -1e-6 < x and x < 1e-6
    # replace with x == 0 si we are handling Fraction elements


GJ_ZERO_SOLUTIONS = 0
GJ_SINGLE_SOLUTION = 1
GJ_SEVERAL_SOLUTIONS = 2


def gauss_jordan(A, x, b):
    """Linear equation system Ax=b by Gauss-Jordan

    :param A: n by m matrix
    :param x: table of size n
    :param b: table of size m
    :modifies: x will contain solution if any
    :returns int:
          0 if no solution,
          1 if solution unique,
          2 otherwise
    :complexity: :math:`O(n^2m)`
    """
    n = len(x)
    m = len(b)
    assert len(A) == m and len(A[0]) == n
    S = []                        # put linear system in a single matrix S
    for i in range(m):
        S.append(A[i][:] + [b[i]])
    S.append(list(range(n)))      # indices in x
    k = diagonalize(S, n, m)
    if k < m:
        for i in range(k, m):
            if not is_zero(S[i][n]):
                return GJ_ZERO_SOLUTIONS
    for j in range(k):
        x[S[m][j]] = S[j][n]
    if k < n:
        for j in range(k, n):
            x[S[m][j]] = 0
        return GJ_SEVERAL_SOLUTIONS
    return GJ_SINGLE_SOLUTION


def diagonalize(S, n, m):
    for k in range(min(n, m)):
        val, i, j = max((abs(S[i][j]), i, j)
                        for i in range(k, m) for j in range(k, n))
        if is_zero(val):
            return k
        S[i], S[k] = S[k], S[i]    # swap lines k, i
        for r in range(m + 1):     # swap columns k, j
            S[r][j], S[r][k] = S[r][k], S[r][j]
        pivot = float(S[k][k])     # without float if Fraction elements
        for j in range(k, n + 1):
            S[k][j] /= pivot       # divide line k by pivot
        for i in range(m):         # remove line k weighted with line i
            if i != k:
                fact = S[i][k]
                for j in range(k, n + 1):
                    S[i][j] -= fact * S[k][j]
    return min(n, m)
# snip}
