#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fenwick tree
# jill-jenn vie et christoph durr - 2014-2018


# snip{
class Fenwick:
    """maintains a tree to allow quick updates and queries
    """
    def __init__(self, t):
        """stores an integer table t, index 0 is ignored

        :param array t: of positive length
        """
        self.s = [0] * len(t)
        for i in range(1, len(t)):
            self.add(i, t[i])

    def prefixSum(self, i):
        """
        :param int i: non negative
        :returns: t[1] + ... + t[i]
        """
        sum = 0
        while i > 0:
            sum += self.s[i]
            i -= (i & -i)
        return sum

    def intervalSum(self, a, b):
        """
        :param int a b: with 1 <= a <= b
        :returns: t[a] + ... + t[b]
        """
        return self.prefixSum(b) - self.prefixSum(a-1)

    def add(self,  i, val):
        """
        :param int i: positive
        :modifies: adds val to t[i]
        """
        assert i > 0
        while i < len(self.s):
            self.s[i] += val
            i += (i & -i)

    # variante:

    def intervalAdd(self, a, b, val):
        """Variant, adds val to t[a], to t[a + 1] ... and to t[b]

        :param int a b: with 1 <= a <= b
        """
        self.add(a,     +val)
        self.add(b + 1, -val)

    def get(self, i):
        """Variant, reads t[i]

        :param int i: positive
        """
        return self.prefixSum(i)
# snip}
