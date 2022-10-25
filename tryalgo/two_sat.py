#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Solving 2-SAT boolean formulas

jill-jenn vie et christoph durr - 2015-2019
"""

from tryalgo.strongly_connected_components import tarjan


# snip{
def _vertex(lit):  # integer encoding of a litteral
    if lit > 0:
        return 2 * (lit - 1)
    return 2 * (-lit - 1) + 1


def two_sat(formula):
    """Solving a 2-SAT boolean formula

    :param formula: list of clauses, a clause is pair of literals
                    over X1,...,Xn for some n.
                    a literal is an integer, for example -1 = not X1, 3 = X3
    :returns: table with boolean assignment satisfying the formula or None
    :complexity: linear
    """
    # num_variables is the number of variables
    num_variables = max(abs(clause[p])
                        for p in (0, 1) for clause in formula)
    graph = [[] for node in range(2 * num_variables)]
    for x_idx, y_idx in formula:                           # x_idx or y_idx
        graph[_vertex(-x_idx)].append(_vertex(y_idx))     # -x_idx => y_idx
        graph[_vertex(-y_idx)].append(_vertex(x_idx))     # -y_idx => x_idx
    sccp = tarjan(graph)
    comp_id = [None] * (2 * num_variables)  # each node's component ID
    assignment = [None] * (2 * num_variables)
    for component in sccp:
        rep = min(component)             # representative of the component
        for vtx in component:
            comp_id[vtx] = rep
            if assignment[vtx] is None:
                assignment[vtx] = True
                assignment[vtx ^ 1] = False    # complementary literal
    for i in range(num_variables):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            return None                        # insatisfiable formula
    return assignment[::2]
# snip}
