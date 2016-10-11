#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exact set cover by the dancing links algorithm
# jill-jenn vie et christoph durr - 2014-2015

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
def cover(c):            # c = l'en-tête de la colonne à cacher
    assert c.C is None   # doit être une cellule d'en-tête
    c.hide_horiz()
    i = c.D
    while i != c:
        j = i.R
        while j != i:
            j.hide_verti()
            j.C.S -= 1   # une entrée de moins dans cette colonne
            j = j.R
        i = i.D


def uncover(c):
    assert c.C is None
    i = c.U
    while i != c:
        j = i.L
        while j != i:
            j.C.S += 1   # une entrée de plus dans cette colonne
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
    header = Cell(None, None, 0, None)  # constr. la structure des cellules
    col = []
    for j in range(size_universe):
        col.append(Cell(header, None, 0, None))
    for i in range(len(sets)):
        row = None
        for j in sets[i]:
            col[j].S += 1               # une entrée de plus dans cette col.
            row = Cell(row, col[j], i, col[j])
    sol = []
    if solve(header, sol):
        return sol
    else:
        return None


def solve(header, sol):
    if header.R == header:     # instance vide, solution trouvée
        return True
    c = None                   # chercher colonne la moins couverte
    j = header.R
    while j != header:
        if c is None or j.S < c.S:
            c = j
        j = j.R
    cover(c)                   # couvrir cette colonne
    r = c.D                    # essayer chaque ligne
    while r != c:
        sol.append(r.S)
        j = r.R                # couvrir éléments dans l'ensemble r
        while j != r:
            cover(j.C)
            j = j.R
        if solve(header, sol):
            return True
        j = r.L                # restituer
        while j != r:
            uncover(j.C)
            j = j.L
        sol.pop()
        r = r.D
    uncover(c)
    return False
# snip}



