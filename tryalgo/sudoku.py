#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Solving Sudoku
# jill-jenn vie et christoph durr - 2014-2018

from tryalgo.dancing_links import dancing_links


__all__ = ["sudoku"]

# snip{
N = 3        # global constants
N2 = N * N
N4 = N2 * N2

# sets
def assignation(r, c, v): return r * N4 + c * N2 + v

def row(a): return a // N4
def col(a): return (a // N2) % N2
def val(a): return a % N2
def blk(a): return (row(a) // N) * N + col(a) // N

# les éléments à couvrir
def rc(a): return row(a) * N2 + col(a)
def rv(a): return row(a) * N2 + val(a) + N4
def cv(a): return col(a) * N2 + val(a) + 2 * N4
def bv(a): return blk(a) * N2 + val(a) + 3 * N4


def sudoku(G):
    """Solving Sudoku

    :param G: integer matrix with 0 at empty cells
    :returns bool: True if grid could be solved
    :modifies: G will contain the solution
    :complexity: huge, but linear for usual published 9x9 grids
    """
    global N, N2, N4
    if len(G) == 16:              # for a 16 x 16 sudoku grid
        N, N2, N4 = 4, 16, 256
    e = 4 * N4
    universe = e + 1
    S = [[rc(a), rv(a), cv(a), bv(a)] for a in range(N4 * N2)]
    A = [e]
    for r in range(N2):
        for c in range(N2):
            if G[r][c] != 0:
                a = assignation(r, c, G[r][c] - 1)
                A += S[a]
    sol = dancing_links(universe, S + [A])
    if sol:
        for a in sol:
            if a < len(S):
                G[row(a)][col(a)] = val(a) + 1
        return True
    else:
        return False
# snip}
