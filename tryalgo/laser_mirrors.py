#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Orienting mirrors to allow connectivity by a laser beam
# jill-jenn vie et christoph durr - 2014-2018

# snip{ laser-miroir-preparation
# directions
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
# orientations None:? 0:/ 1:\

# destination UP          LEFT         DOWN           RIGHT
reflex = [[RIGHT, LEFT], [DOWN, UP],  [LEFT, RIGHT], [UP, DOWN]]


def laser_mirrors(rows, cols, mir):
    """Orienting mirrors to allow reachability by laser beam

    :param int rows:
    :param int cols: rows and cols are the dimension of the grid
    :param mir: list of mirror coordinates, except
                mir[0]= laser entrance,
                mir[-1]= laser exit.
    :complexity: :math:`O(2^n)`
    """
    # build structures
    n = len(mir)
    orien = [None] * (n + 2)
    orien[n] = 0      # arbitrary orientations
    orien[n + 1] = 0
    succ = [[None for direc in range(4)] for i in range(n + 2)]
    L = [(mir[i][0], mir[i][1], i) for i in range(n)]
    L.append((0, -1, n))                  # enter
    L.append((0, cols, n + 1))            # exit
    last_r, last_i = None, None
    for (r, c, i) in sorted(L):           # sweep by row
        if last_r == r:
            succ[i][LEFT] = last_i
            succ[last_i][RIGHT] = i
        last_r, last_i = r, i
    last_c = None
    for (r, c, i) in sorted(L, key=lambda tup_rci: (tup_rci[1], tup_rci[0])):
        if last_c == c:                   # sweep by column
            succ[i][UP] = last_i
            succ[last_i][DOWN] = i
        last_c, last_i = c, i
    if solve(succ, orien, n, RIGHT):      # exploration
        return orien[:n]
    else:
        return None
# snip}


# snip{ laser-miroir-exploration
def solve(succ, orien, i, direc):
    """Can a laser leaving mirror i in direction direc reach exit ?

    :param i: mirror index
    :param direc: direction leaving mirror i
    :param orient: orient[i]=orientation of mirror i
    :param succ: succ[i][direc]=succ mirror reached
                 when leaving i in direction direc
    """
    assert orien[i] != None
    j = succ[i][direc]
    if j is None:          # basic case
        return False
    if j == len(orien) - 1:
        return True
    if orien[j] is None:   # try both orientations
        for x in [0, 1]:
            orien[j] = x
            if solve(succ, orien, j, reflex[direc][x]):
                return True
        orien[j] = None
        return False
    else:
        return solve(succ, orien, j, reflex[direc][orien[j]])
# snip}
