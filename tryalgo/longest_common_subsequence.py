#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Longest increasing subsequence
# jill-jenn vie et christoph durr - 2014-2018


# snip{
def longest_common_subsequence(x, y):
    """Longest common subsequence

    Dynamic programming

    :param x:
    :param y: x, y are lists or strings
    :returns: longest common subsequence in form of a string
    :complexity: `O(|x|*|y|)`
    """
    n = len(x)
    m = len(y)
    #                      -- compute optimal length
    A = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                A[i + 1][j + 1] = A[i][j] + 1
            else:
                A[i + 1][j + 1] = max(A[i][j + 1],  A[i + 1][j])
    #                      -- extract solution
    sol = []
    i, j = n, m
    while A[i][j] > 0:
        if A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            sol.append(x[i])
    return ''.join(sol[::-1])    # inverse solution
# snip}
