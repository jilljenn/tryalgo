#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Solving 2-SAT boolean formulas
# jill-jenn vie et christoph durr - 2015-2018

from tryalgo.strongly_connected_components import tarjan


# snip{
def _vertex(lit):  # integer encoding of a litteral
    if lit > 0:
        return 2 * (lit - 1)
    else:
        return 2 * (-lit - 1) + 1


def two_sat(formula):
    """Solving a 2-SAT boolean formula

    :param formula: list of clauses, a clause is pair of literals
                    over X1,...,Xn for some n.
                    a literal is an integer, for example -1 = not X1, 3 = X3
    :returns: table with boolean assignment satisfying the formula or None
    :complexity: linear
    """
    #                                   -- n is the number of variables
    n = max(abs(clause[p]) for p in (0, 1) for clause in formula)
    graph = [[] for node in range(2 * n)]
    for x, y in formula:                           # x or y
        graph[_vertex(-x)].append(_vertex(y))      # -x => y
        graph[_vertex(-y)].append(_vertex(x))      # -y => x
    sccp = tarjan(graph)
    comp_id = [None] * (2 * n)     # for each node the ID of its component
    assignment = [None] * (2 * n)
    for component in sccp:
        rep = min(component)             # representative of the component
        for vtx in component:
            comp_id[vtx] = rep
            if assignment[vtx] is None:
                assignment[vtx] = True
                assignment[vtx ^ 1] = False    # complementary literal
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            return None                        # insatisfiable formula
    return assignment[::2]
# snip}
