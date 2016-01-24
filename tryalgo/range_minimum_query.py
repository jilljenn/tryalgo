#!/usr/bin/env python3
# Range minimum query
# Minimum d'une plage --- range minimum query
# jill-jenn vie et christoph durr - 2014-2015


# snip{
class RangeMinQuery:
    """Range minimum query

    maintains a table t, can read/write items t[i],
    and query range_min(i,k) = min{ t[i], t[i + 1], ..., t[k - 1]}
    :complexity: all operations in O(log n), for n = len(t)
    """
    def __init__(self, t, INF=float('inf')):
        self.INF = INF
        self.N = 1
        while self.N < len(t):                     # trouver la taille N
            self.N *= 2
        self.s = [self.INF] * (2 * self.N)
        for i in range(len(t)):                    # poser t aux feuilles
            self.s[self.N + i] = t[i]
        for p in range(self.N - 1, 0, -1):         # remplir les noeuds
            self.s[p] = min(self.s[2 * p], self.s[2 * p + 1])

    def __getitem__(self, i):
        return self.s[self.N + i]

    def __setitem__(self, i, v):
        """ sets t[i] to v.
            :complexity: O(log len(t))
        """
        p = self.N + i
        self.s[p] = v
        p //= 2                                    # remonter dans l'arbre
        while p > 0:                               # mettre à jour le noeud
            self.s[p] = min(self.s[2 * p], self.s[2 * p + 1])
            p //= 2

    def range_min(self, i, k):
        """:returns:  min{ t[i], t[i + 1], ..., t[i + k - 1]}
        :complexity: O(log len(t))
        """
        return self._range_min(1, 0, self.N, i, k)

    def _range_min(self, p, start, span, i, k):
        """returns the minimum in t in the indexes [i, k) intersected
           with [start, start + span).
           p is the node associated to the later interval.
        """
        if start + span <= i or k <= start:        # intervalles disjoints
            return self.INF
        if i <= start and start + span <= k:       # intervalles inclus
            return self.s[p]
        left = self._range_min(2*p,      start,             span // 2, i, k)
        right = self._range_min(2*p + 1, start + span // 2, span // 2, i, k)
        return min(left, right)
# snip}
