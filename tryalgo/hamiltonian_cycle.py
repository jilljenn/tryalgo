#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Hamiltonian Cycle

jill-jenn vie et christoph durr - 2023
"""


# snip{ 
def hamiltonian_cycle(weight):
    """Hamiltonian Cycle

    :param weight: matrix of edge weights of a complete graph
    :returns: minimum weight of a Hamiltonian cycle
    :complexity: O(n^2 2^n)
    """
    n = len(weight)
    # A[S][v] = minimum weight path from vertex n-1, 
    #           then visiting all vertices in S exactly once, 
    #           and finishing in v (which is not in S)
    A = [[float('inf')] * n for _ in range(1 << (n - 1))]
    for v in range(n):                  # base case
        A[0][v] = weight[n - 1][v] 
    for S in range(1, 1 << (n - 1)):
        for v in range(n):
            if not ((1 << v) & S):      # v not in S
                for u in range(n - 1):
                    U = 1 << u
                    if U & S:           # u in S
                        alt = A[S ^ U][u] + weight[u][v]
                        if alt < A[S][v]:
                            A[S][v] = alt
    S = (1 << (n - 1)) - 1              # {0, 1, ..., n - 2}
    return A[S][n - 1]
# snip}

