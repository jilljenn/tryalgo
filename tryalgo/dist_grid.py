#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Distances in a grid
# jill-jenn vie et christoph durr - 2014-2015

from collections import deque


# snip{
def dist_grid(grid, source, target=None):
    """Distances in a grid by BFS

    :param grid: matrix with 4-neighborhood
    :param (int,int) source: pair of row, column indices
    :param (int,int) target: exploration stops if target is reached
    :complexity: linear in grid size
    """
    rows = len(grid)
    cols = len(grid[0])
    dir = [(0, +1, '>'), (0, -1, '<'), (+1, 0, 'v'), (-1, 0, '^')]
    i, j = source
    grid[i][j] = 's'
    Q = deque()
    Q.append(source)
    while Q:
        i1, j1 = Q.popleft()
        for di, dj, symbol in dir:   # explorer toutes les directions
            i2 = i1 + di
            j2 = j1 + dj
            if not (0 <= i2 and i2 < rows and 0 <= j2 and j2 < cols):
                continue             # bord de la grille dépassé
            if grid[i2][j2] != ' ':  # case inacc. ou déjà visitée
                continue
            grid[i2][j2] = symbol    # marquer visite
            if (i2, j2) == target:
                grid[i2][j2] = 't'   # but atteint
                return
            Q.append((i2, j2))
# snip}

