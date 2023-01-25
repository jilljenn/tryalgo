#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Dynamic Programming speeup tricks

christoph dürr - jill-jênn vie - 2022
"""

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
    C = [[0 for j in range(n)] for i in range(n)] #
    K = [[i for j in range(n)] for i in range(n)] # initially K[i,i]=i
    
    # recursion
    for j_i in range(1, n): # difference between j and i
        for i in range(n - j_i):
            j = i + j_i
            argmin = None
            valmin = float('+inf')
            for k in range(K[i][j - 1], K[i + 1][j] + 1):
                alt = C[i][k - 1] + C[k][j]
                if alt < valmin:
                    valmin = alt
                    argmin = k
            C[i][j] = W[i][j] + valmin
            K[i][j] = argmin 
     
    return C[0][n - 1], K
