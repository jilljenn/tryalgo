#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Distances in a grid
jill-jenn vie et christoph durr - 2014-2018
--------------------------------------------
"""

from collections import deque


# snip{
def dist_grid(grid, source, target=None):
    """Distances in a grid by BFS

    :param grid: matrix with 4-neighborhood
    :param (int,int) source: pair of row, column ind_ices
    :param (int,int) target: exploration stops if target is reached
    :complexity: linear in grid size
    """
    rows = len(grid)
    cols = len(grid[0])
    i, j = source
    grid[i][j] = 's'
    q_ueue = deque()
    q_ueue.append(source)
    while q_ueue:
        i_1, j_1 = q_ueue.popleft()
        for d_i, d_j, symbol in [(0, +1, '>'),
                                 (0, -1, '<'),
                                 (+1, 0, 'v'),
                                 (-1, 0, '^')]:   # explore all d_irections
            i_2 = i_1 + d_i
            j_2 = j_1 + d_j
            if not (0 <= i_2 < rows and 0 <= j_2 < cols):
                continue                # reached the bounds of the grid
            if grid[i_2][j_2] != ' ':   # inaccessible or already visited
                continue
            grid[i_2][j_2] = symbol     # mark visit
            if (i_2, j_2) == target:
                grid[i_2][j_2] = 't'    # goal is reached
                return
            q_ueue.append((i_2, j_2))
# snip}
