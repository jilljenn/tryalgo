#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exact set cover by the dancing links algorithm
# jill-jenn vie et christoph durr - 2014-2018

__all__ = ["dancing_links"]


# snip{ liens-dansants-cell
class Cell:
    def __init__(self, horiz, verti, S, C):
        self.S = S
        self.C = C
        if horiz:
            self.L = horiz.L
            self.R = horiz
            self.L.R = self
            self.R.L = self
        else:
            self.L = self
            self.R = self
        if verti:
            self.U = verti.U
            self.D = verti
            self.U.D = self
            self.D.U = self
        else:
            self.U = self
            self.D = self

    def hide_verti(self):
        self.U.D = self.D
        self.D.U = self.U

    def unhide_verti(self):
        self.D.U = self
        self.U.D = self

    def hide_horiz(self):
        self.L.R = self.R
        self.R.L = self.L

    def unhide_horiz(self):
        self.R.L = self
        self.L.R = self
# snip}


# snip{ liens-dansants-cover
def cover(c):            # c = heading cell of the column to cover
    assert c.C is None   # must be a heading cell
    c.hide_horiz()
    i = c.D
    while i != c:
        j = i.R
        while j != i:
            j.hide_verti()
            j.C.S -= 1   # one fewer entry in this column
            j = j.R
        i = i.D


def uncover(c):
    assert c.C is None
    i = c.U
    while i != c:
        j = i.L
        while j != i:
            j.C.S += 1   # one more entry in this column
            j.unhide_verti()
            j = j.L
        i = i.U
    c.unhide_horiz()
# snip}


# snip{ liens-dansants-exploration
def dancing_links(size_universe, sets):
    """Exact set cover by the dancing links algorithm

    :param size_universe: universe = {0, 1, ..., size_universe - 1}
    :param sets: list of sets
    :returns: list of set indices partitioning the universe, or None
    :complexity: huge
    """
    header = Cell(None, None, 0, None)  # building the cell structure
    col = []
    for j in range(size_universe):
        col.append(Cell(header, None, 0, None))
    for i in range(len(sets)):
        row = None
        for j in sets[i]:
            col[j].S += 1               # one more entry in this column
            row = Cell(row, col[j], i, col[j])
    sol = []
    if solve(header, sol):
        return sol
    else:
        return None


def solve(header, sol):
    if header.R == header:     # the instance is empty => solution found
        return True
    c = None                   # find the least covered column
    j = header.R
    while j != header:
        if c is None or j.S < c.S:
            c = j
        j = j.R
    cover(c)                   # cover this column
    r = c.D                    # try every row
    while r != c:
        sol.append(r.S)
        j = r.R                # cover elements in set r
        while j != r:
            cover(j.C)
            j = j.R
        if solve(header, sol):
            return True
        j = r.L                # uncover
        while j != r:
            uncover(j.C)
            j = j.L
        sol.pop()
        r = r.D
    uncover(c)
    return False
# snip}
