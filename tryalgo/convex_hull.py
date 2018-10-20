#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Convex hull by Andrew
# jill-jenn vie et christoph durr - 2014-2018

from random import randint


__all__ = ["andrew"]


# snip{ left-turn
def left_turn(a, b, c):
    return ((a[0] - c[0]) * (b[1] - c[1]) -
            (a[1] - c[1]) * (b[0] - c[0]) > 0)
# snip}


# snip{
def andrew(S):
    """Convex hull by Andrew

    :param S: list of points as coordinate pairs
    :requires: S has at least 2 points
    :returns: list of points of the convex hull
    :complexity: `O(n log n)`
    """
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top) >= 2 and not left_turn(p, top[-1], top[-2]):
            top.pop()
        top.append(p)
        while len(bot) >= 2 and not left_turn(bot[-2], bot[-1], p):
            bot.pop()
        bot.append(p)
    return bot[:-1] + top[:0:-1]
# snip}


if __name__ == "__main__":

    def gnuplot(L):
        for x, y in L:
            print(x, y)
        print

    def tikz_points(S):
        for p in S:
            print('\\filldraw[black] (%f, %f) circle (1pt);' % p)

    def tikz_polygone(S):
        for i in range(len(S)):
            print('\\draw[blue] (%f, %f) -- (%f, %f);' % (S[i - 1] + S[i]))

    S = [(randint(0, 25)/10., randint(0, 25)/10.) for _ in range(32)]
    tikz_points(S)
    tikz_polygone(andrew(S))
