#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Closest pair of points
# trouver la paire de points la plus proche
# jill-jenn vie et christoph durr et louis abraham - 2014-2018


from random import randint


# snip{
from math import hypot   # hypot(dx, dy) = sqrt(dx * dx + dy * dy)
from random import shuffle

__all__ = ["closest_points"]


def dist(p, q):
    return hypot(p[0] - q[0], p[1] - q[1])


def cell(point, pas):
    x, y = point
    # beware: in other languages negative coordinates need special care
    # in C++ for example int(-1.5) == -1 and not -2 as we need
    return (int(x // pas), int(y // pas))


def improve(S, d):
    G = {}            # grid
    for p in S:
        a, b = cell(p, d / 2)
        for a1 in range(a - 2, a + 3):
            for b1 in range(b - 2, b + 3):
                if (a1, b1) in G:
                    q = G[a1, b1]
                    pq = dist(p, q)
                    if pq < d:
                        return pq, p, q
        G[a, b] = p
    return None


def closest_points(S):
    """Closest pair of points

    :param S: list of points
    :requires: size of S at least 2
    :modifies: changes the order in S
    :returns: pair of points p,q from S with minimum Euclidean distance
    :complexity: expected linear time
    """
    shuffle(S)
    assert len(S) >= 2
    p = S[0]
    q = S[1]
    d = dist(p, q)
    while d > 0:
        r = improve(S, d)
        if r:
            d, p, q = r
        else:
            break
    return p, q
# snip}


if __name__ == "__main__":

    def tikz_points(S):
        for p in S:
            print("\\filldraw[black] (%f, %f) circle (1pt);" % p)

    def tikz_polygone(S):
        for i in range(len(S)):
            print('\\draw (%f, %f) -- (%f, %f);' % (S[i - 1] + S[i]))

    S = [(randint(0, 400) / 100, randint(0, 400) / 100) for _ in range(32)]
    tikz_points(S)
    tikz_polygone(closest_points(S))
