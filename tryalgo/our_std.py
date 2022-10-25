#!/usr/bin/env python3
# coding=utf8
"""\
Our Standards

Jill-Jênn Vie et Christoph Dürr - 2020
"""
from sys import stdin


def readint():
    """
    function to read an integer from stdin
    """
    return int(stdin.readline())


def readstr():
    """
    function to read a string from stdin
    """
    return stdin.readline().strip()


def readarray(typ):
    """
    function to read an array
    """
    return list(map(typ, stdin.readline().split()))


# pylint: disable=redefined-outer-name
def readmatrix(n):
    """
    function to read a matrix
    """
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M
