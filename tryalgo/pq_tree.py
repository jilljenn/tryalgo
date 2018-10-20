#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# c.durr - 2017-2018


""" Solve the consecutive all ones column problem using PQ-trees

    In short, a PQ-tree represents sets of total orders over a ground set. The
    leafs are the values of the ground set. Inner nodes are of type P or Q. P
    means all permutations of the children are allowed. Q means only the left
    to right or the right to left order of the children is allowed.

    The method restrict(S), changes the tree such that it represents only
    total orders which would leave the elements of the set S consecutive.  The
    complexity of restrict is linear in the tree size.

    References:

    [W] https://en.wikipedia.org/wiki/PQ_tree

    [L10] Richard Ladner, slides.
        https://courses.cs.washington.edu/courses/cse421/10au/lectures/PQ.pdf

    [H00] Mohammad Taghi Hajiaghayi, notes.
        http://www-math.mit.edu/~hajiagha/pp11.ps


    Disclaimer: this implementation does not have the optimal time complexity.
    And also there are more recent and easier algorithms for this problem.

"""


from collections import deque


class IsNotC1P(Exception):
    """The given instance does not have the all consecutive ones property"""
    pass


P_shape = 0
Q_shape = 1
L_shape = 2

EMPTY = 0
FULL = 1
PARTIAL = 2

# automaton is used for pattern recognition when reducing a Q node
# -1 represents the result of a forbidden transition
#             E  F  P
automaton = [[1, 5, 4],  # 0 initial state
             [1, 2, 2],  # 1
             [3, 2, 3],  # 2
             [3,-1,-1],  # 3
             [6, 2, 3],  # 4
             [6, 5, 6],  # 5
             [6,-1,-1]]  # 6


class PQ_node:

    def __init__(self, shape, value=None):
        self.shape = shape
        self.sons = []
        self.parent = None
        self.value = value
        self.full_leafs = 0
        self.processed_sons = 0
        self.mark = EMPTY

    def add(self, node):
        """Add one node as descendant
        """
        self.sons.append(node)
        node.parent = self

    def add_all(self, L):
        for x in L:
            self.add(x)

    def add_group(self, L):
        """Add elements of L as descendants of the node.
        If there are several elements in L, group them in a P-node first
        """
        if len(L) == 1:
            self.add(L[0])
        elif len(L) >= 2:
            x = PQ_node(P_shape)
            x.add_all(L)
            self.add(x)
        # nothing to be done for an empty list L

    def border(self, L):
        """Append to L the border of the subtree.
        """
        if self.shape == L_shape:
            L.append(self.value)
        else:
            for x in self.sons:
                x.border(L)

    def __str__(self):
        if self.shape == L_shape:
            return str(self.value)
        for x in self.sons:
            assert x.parent == self
        if self.shape == P_shape:
            return "(" + ",".join(map(str, self.sons)) + ")"
        else:
            return "[" + ",".join(map(str, self.sons)) + "]"


class PQ_tree:

    def __init__(self, universe):
        self.tree = PQ_node(P_shape)
        self.leafs = []
        for i in universe:
            x = PQ_node(L_shape, value=i)
            self.tree.add(x)
            self.leafs.append(x)

    def __str__(self):
        """returns a string representation,
        () for P nodes and [] for Q nodes
        """
        return str(self.tree)

    def border(self):
        """returns the list of the leafs in order
        """
        L = []
        self.tree.border(L)
        return L

    def reduce(self, S):
        queue = deque(self.leafs)
        cleanup = []                        # we don't need to cleanup leafs
        is_key_node = False
        while queue and not is_key_node:    # while there are nodes to be processed
            x = queue.popleft()
            is_key_node = (x.full_leafs == len(S))
            x.mark = PARTIAL                # default mark
            if x.shape == P_shape:
                E = []                      # group descendants according to marks
                F = []
                P = []
                for y in x.sons:
                    if y.mark == EMPTY:
                        E.append(y)
                    elif y.mark == FULL:
                        F.append(y)
                    else:
                        P.append(y)
                if len(P) == 0:       # start long case analysis
                    if len(E) == 0:
                        x.mark = FULL
                    else:
                        if len(F) == 0:
                            # template P1
                            x.mark = EMPTY
                        else:
                            if is_key_node:
                                # template P2
                                x.sons = E
                                x.add_group(F)
                            else:                    # is not root
                                # template P3
                                x.shape = Q_shape
                                x.sons = []
                                x.add_group(E)
                                x.add_group(F)
                elif len(P) == 1:
                    assert P[0].shape == Q_shape
                    if is_key_node:
                        # template P4
                        x.sons = E + [P[0]]
                        P[0].add_group(F)
                    else:                        # is not root
                        # template P5
                        x.shape = Q_shape
                        x.sons = []
                        x.add_group(E)
                        x.add_all(P[0].sons)
                        x.add_group(F)
                elif len(P) == 2:
                    if is_key_node:
                        # template P6
                        x.sons = E
                        z = P[0]
                        z.add_group(F)
                        z.add_all(reversed(P[1].sons))
                    else:
                        raise IsNotC1P
                else:                      # more than 2 partial descendants
                    raise IsNotC1P
            elif x.shape == Q_shape:
                state = 0
                L = []
                for y in x.sons:
                    previous = state
                    state = automaton[state][y.mark]
                    if state == -1:
                        raise IsNotC1P
                    elif (state == 3 or state == 6) and y.mark == PARTIAL:
                        assert y.shape == Q_shape
                        L += reversed(y.sons)
                    elif state == 6 and previous == 4:
                        L = L[::-1]
                        L.append(y)
                    elif y.mark == PARTIAL:
                        L += y.sons
                    else:
                        L.append(y)
                if state == 3 and not is_key_node:
                    raise IsNotC1P
                elif state == 5:
                    x.mark = FULL
                x.sons = []
                if state == 6:
                    x.add_all(reversed(L))
                else:
                    x.add_all(L)
            else:                           # x is a leaf
                if x.value in S:
                    x.mark = FULL
                    x.full_leafs = 1
                else:
                    x.mark = EMPTY
                    x.full_leafs = 0
            if not is_key_node:                              # propagate node processing
                z = x.parent
                z.full_leafs += x.full_leafs                 # cumulate bottom up full leaf numbers
                if z.processed_sons == 0:
                    cleanup.append(z)                        # first time considered
                z.processed_sons += 1
                if z.processed_sons == len(z.sons):
                    queue.append(z)                          # otherwise prune tree at z
        for x in cleanup:
            x.full_leafs = 0
            x.processed_sons = 0
            x.mark = EMPTY


def consecutive_ones_property(sets, universe=None):
    """ Check the consecutive ones property.

    :param list sets: is a list of subsets of the ground set.
    :param groundset: is the set of all elements,
                by default it is the union of the given sets
    :returns: returns a list of the ordered ground set where
              every given set is consecutive,
              or None if there is no solution.
    :complexity: O(len(groundset) * len(sets))
    :disclaimer: an optimal implementation would have complexity
                 O(len(groundset) + len(sets) + sum(map(len,sets))),
                 and there are more recent easier algorithms for this problem.
    """
    if universe is None:
        universe = set()
        for S in sets:
            universe |= set(S)
    tree = PQ_tree(universe)
    try:
        for S in sets:
            tree.reduce(S)
        return tree.border()
    except IsNotC1P:
        return None
