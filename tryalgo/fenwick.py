#!/usr/bin/env python3
# Fenwick tree
# jill-jenn vie et christoph durr - 2014-2015


# snip{
class Fenwick:
    """Fenwick tree
       maintains a tree to allow quick updates and queries
    """
    def __init__(self, t):
        """stores an integer table t, index 0 is ignored
        """
        self.s = [0] * len(t)
        for i in range(1, len(t)):
            self.add(i, t[i])

    def prefixSum(self, i):
        """:returns: t[1] + ... + t[i]
        """
        sum = 0
        while i > 0:
            sum += self.s[i]
            i -= (i & -i)
        return sum

    def intervalSum(self, a, b):
        """:returns: t[a] + ... + t[b]
        """
        return self.prefixSum(b) - self.prefixSum(a-1)

    def add(self,  i, val):
        """:modifies: adds val to t[i]
        """
        assert i > 0
        while i < len(self.s):
            self.s[i] += val
            i += (i & -i)

    # variante:

    def intervalAdd(self, a, b, val):
        """Variant, adds val to t[a], to t[a + 1] ... and to t[b]
        """
        self.add(a,     +val)
        self.add(b + 1, -val)

    def get(self, i):
        """Variant, reads t[i]
        """
        return self.prefixSum(i)
# snip}

