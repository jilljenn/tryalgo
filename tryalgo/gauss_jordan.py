#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Linear equation system Ax=b by Gauss-Jordan
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def is_zero(x):                    # tolérance
    """error tolerant zero test
    """
    return -1e-6 < x and x < 1e-6
    # remplacer par x == 0 si on travaille avec Fractions

GJ_ZERO_SOLUTIONS = 0              # codes retour
GJ_UNE_SOLUTION = 1
GJ_PLUSIEURS_SOLUTIONS = 2


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
    S = []                # mettre système dans une unique matrice S
    for i in range(m):
        S.append(A[i][:] + [b[i]])
    S.append(list(range(n)))       # indices dans x
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
        return GJ_PLUSIEURS_SOLUTIONS
    return GJ_UNE_SOLUTION


def diagonalize(S, n, m):
    for k in range(min(n, m)):
        val, i, j = max((abs(S[i][j]), i, j)
                        for i in range(k, m) for j in range(k, n))
        if is_zero(val):
            return k
        S[i], S[k] = S[k], S[i]    # échanger lignes   k, i
        for r in range(m + 1):       # échanger colonnes k, j
            S[r][j], S[r][k] = S[r][k], S[r][j]
        pivot = float(S[k][k])     # sans float si on trav. avec Fractions
        for j in range(k, n + 1):
            S[k][j] /= pivot       # diviser ligne k par pivot
        for i in range(m):         # enlever ligne k pondérée de la ligne i
            if i != k:
                fact = S[i][k]
                for j in range(k, n + 1):
                    S[i][j] -= fact * S[k][j]
    return min(n, m)
# snip}
