#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
c.durr, a.durr - 2017-2019


    Solve the consecutive all ones column problem using PQ-trees

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
# pylint: disable=bad-whitespace, missing-docstring, len-as-condition
# pylint: disable=too-many-nested-blocks, no-else-raise, too-many-branches

from collections import deque

class IsNotC1P(Exception):
    """The given instance does not have the all consecutive ones property"""


P_shape = 0
Q_shape = 1
L_shape = 2

EMPTY = 0
FULL = 1
PARTIAL = 2

# automaton is used for pattern recognition when reducing a Q node
# -1 represents the result of a forbidden transition
#             E   F   P
automaton = [[1,  5,  4],  # 0 initial state
             [1,  2,  2],  # 1
             [3,  2,  3],  # 2
             [3, -1, -1],  # 3
             [6,  2,  3],  # 4
             [6,  5,  6],  # 5
             [6, -1, -1]]  # 6


class PQNode:

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
            x = PQNode(P_shape)
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
        m = ["", "*", "+"][self.mark]
        if self.shape == L_shape:
            return m + str(self.value)
        L = ",".join(map(str, self.sons))
        if self.shape == P_shape:
            return "{}({})".format(m, L)
        return "{}[{}]".format(m, L)

    def representation(self):
        if self.shape == L_shape:
            return str(self.value)
        # assert self.processed_sons == 0 
        # assert self.full_leafs == 0 
        # assert self.mark == EMPTY
        if self.shape == P_shape:
            return tuple(x.representation() for x in self.sons)
        return list(x.representation() for x in self.sons)


# pylint: disable=too-many-statements
class PQTree:

    def __init__(self, universe):
        self.tree = PQNode(P_shape)
        self.leafs = []
        for i in universe:
            x = PQNode(L_shape, value=i)
            self.tree.add(x)
            self.leafs.append(x)

    def __str__(self):
        """returns a string representation,
        () for P nodes and [] for Q nodes
        """
        return str(self.tree)

    def representation(self):
        return self.tree.representation()

    def border(self):
        """returns the list of the leafs in order
        """
        L = []
        self.tree.border(L)
        return L

    def reduce(self, S):
        queue = deque(self.leafs)
        cleanup = []                        # we don't need to cleanup leafs
        x_is_key_node = False
        while queue and not x_is_key_node:  # while there are nodes to process
            x = queue.popleft()
            x_is_key_node = (x.full_leafs == len(S))
            x.mark = PARTIAL              # default mark
            # print(f"reducing with {S} self={self} x={x} is key node={x_is_key_node}")
            if x.shape == P_shape:                # ------------------------ P shape
                group = [[], [], []]
                for y in x.sons:
                    group[y.mark].append(y)
                # print("numbers of sons empty={}, full={}, partial={}".format(*map(len, group)))
                if len(group[PARTIAL]) == 0:       # start long case analysis
                    if len(group[EMPTY]) == 0:
                        x.mark = FULL
                    else:
                        if len(group[FULL]) == 0:
                            # template P1
                            x.mark = EMPTY
                            template = "P1"
                        else:
                            if x_is_key_node:
                                # template P2
                                x.sons = group[EMPTY]
                                x.add_group(group[FULL])
                                template = "P2"
                            else:                    # is not root
                                # template P3
                                x.shape = Q_shape
                                x.sons = []
                                x.add_group(group[EMPTY])
                                x.add_group(group[FULL])
                                template = "P3"
                elif len(group[PARTIAL]) == 1:
                    z = group[PARTIAL][0]
                    assert z.shape == Q_shape
                    if x_is_key_node:
                        # template P4
                        x.sons = group[EMPTY] + [z]
                        z.add_group(group[FULL])
                        template = "P4"
                    else:                        # is not root
                        # template P5
                        x.shape = Q_shape
                        x.sons = []
                        x.add_group(group[EMPTY])
                        x.add_all(z.sons)
                        x.add_group(group[FULL])
                        template = "P5"
                elif len(group[PARTIAL]) == 2:
                    if x_is_key_node:
                        # template P6
                        x.sons = group[EMPTY]
                        z0, z1 = group[PARTIAL]
                        z0.add_group(group[FULL])
                        z0.add_all(reversed(z1.sons))
                        x.add(z0)
                        template = "P6"
                    else:
                        raise IsNotC1P
                else:                      # more than 2 partial descendants
                    raise IsNotC1P
            elif x.shape == Q_shape:       # ------------------------ Q shape
                state = 0
                L = []
                for y in x.sons:
                    previous = state
                    state = automaton[state][y.mark]
                    if state == -1:
                        raise IsNotC1P
                    elif (state in (3, 6)) and y.mark == PARTIAL:
                        assert y.shape == Q_shape
                        L += reversed(y.sons)
                    elif state == 6 and previous == 4:
                        L = L[::-1]
                        L.append(y)
                    elif y.mark == PARTIAL:
                        L += y.sons
                    else:
                        L.append(y)
                if state == 3 and not x_is_key_node:
                    raise IsNotC1P
                elif state == 5:
                    x.mark = FULL
                    template = "Q full"
                # print(f"state is {state}")
                if state == 6:
                    x.sons = []
                    x.mark = PARTIAL
                    x.add_all(reversed(L))
                    # template = "Q partial reversed"
                elif state == 1:
                    x.mark = EMPTY
                else:
                    x.sons = []
                    x.mark = PARTIAL
                    x.add_all(L)
                    # template = "Q partial"
            else:                             # ------------------------ leaf
                if x.value in S:
                    x.mark = FULL
                    x.full_leafs = 1
                else:
                    x.mark = EMPTY
                    x.full_leafs = 0
                template = "leaf"
            # print(f"template {template} x={x}")
            if not x_is_key_node:             # propagate node processing
                z = x.parent
                assert z is not None
                z.full_leafs += x.full_leafs  # cumulate bottom-up full numbers
                if z.processed_sons == 0:
                    cleanup.append(z)         # first time considered
                z.processed_sons += 1
                if z.processed_sons == len(z.sons):
                    queue.append(z)           # otherwise prune tree at z
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
    if universe is None:    # no universe provided ?
        universe = set()    # then work the union of the given sets
        for S in sets:
            universe |= set(S)
    tree = PQTree(universe)
    try:
        for S in sets:      # reduce with each given set
            tree.reduce(S)
            # print(str(tree))
        return tree.border()
    except IsNotC1P:
        return None
