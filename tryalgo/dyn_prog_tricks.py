#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Dynamic Programming speedup tricks

christoph dürr - jill-jênn vie - 2022
"""

import sys


def dyn_prog_Monge(W):
    """ Solves the following dynamic program for 0 <= i < j < n

    C[i,i] = 0
    C[i,j] = W[i,j] + min over i < k <= j of (C[i,k-1] + C[k,j]) 
    K[i,j] = minimizer of above

    :param W: matrix of dimension n times n
    :assumes: W satisfies the Monge property (a.k.a. quadrangle inequality) and monotonicity in the lattice of intervals 
    :returns: C[0,n-1] and the matrix K with the minimizers
    :complexity: O(n^2)
    """
    n = len(W) 
    C = [[W[i][i] for j in range(n)] for i in range(n)] # initially C[i,i]=W[i][i]
    K = [[j for j in range(n)] for i in range(n)] # initially K[i,i]=i
    
    # recursion
    for j_i in range(1, n): # difference between j and i
        for i in range(n - j_i):
            j = i + j_i
            argmin = None
            valmin = float('+inf')
            for k in range(max(i + 1, K[i][j - 1]),  K[i + 1][j] + 1):
                alt = C[i][k - 1] + C[k][j]
                if alt < valmin:
                    valmin = alt
                    argmin = k
            C[i][j] = W[i][j] + valmin
            K[i][j] = argmin 
    return C[0][n-1], K


def _decode(i, j, R, level, current):
    """is used by decode_root_matrix_to_level for recursive decoding."""
    if i >= j:
        return # nothing to do
    root = R[i][j]
    level[root] = current
    _decode(i, root-1, R, level, current + 1)
    _decode(root, j, R, level, current + 1)


def decode_root_matrix_to_level(R):
    """Decodes a binary search tree encoded in the root matrix R into a level array
    :returns: the level array
    :complexity: linear
    """
    n = len(R)
    level = [0] * n 
    _decode(0, n - 1, R, level, 0)
    return level[1:]


def opt_bin_search_tree2(success, failure):
    """ Optimal binary search tree on elements from 1 to n
    
    :param success: n+1 dimensional array with frequency of every element i. 
                    success[0] is ignored
    :param failure: n+1 dimensional array with frequency between the elements,
                    failure[i] is frequency of a query strictly between element i and i+1.
                    These arrays do not have to be normalized.
    :returns:       The value of an optimal search tree and the matrix with the roots for each
                    subproblem, encoding the actual tree.
    :complexity: O(n^2)
    """
    n = len(failure)
    N = range(n)
    W = [[failure[i] for j in N] for i in N]
    for i in N:
        for j in range(i+1, n):
            W[i][j] = W[i][j - 1] + failure[j] + success[j]
    return dyn_prog_Monge(W)


def opt_bin_search_tree1(freq):
    """ Optimal binary search tree on elements from 0 to n-1
    
    :param freq: n dimensional array with frequency of every element i. 
    :returns:    The value of an optimal search tree and the matrix with the roots for each
                 subproblem, encoding the actual tree.
    :complexity: O(n^2)
    """
    n = len(freq)
    return opt_bin_search_tree2([0] + freq, [0] * (n + 1))

if  __name__ == "__main__":   

    def readint(): return int(sys.stdin.readline())
    def readstr(): return sys.stdin.readline().strip()
    def readfloats(): return list(map(float, readstr().split()))
 
    n = readint()
    beta = [0] + readfloats()
    alpha = readfloats()
    print(opt_bin_search_tree2(beta, alpha)[0])
    