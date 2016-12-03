#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Solving Horn SAT
# christoph dürr - 2016

"""

clauses are numbered starting from 0
variables are numbered starting from 1

sol : set of variables that are set to true
notsol : set of variables that have to be set to false
posvar_in_clause : maps clause to the unique positive variable in clause (or None)
clause_with_posvar : maps variable v to all clauses that contain v
clause_with_negvar : maps variable v to all clauses that contain not(v)

every clause has a score: number of its negative variables that are not in solution sol
pool : maps score to clauses of that score
"""

from collections import defaultdict
import sys

def read(filename):
    """ reads a Horn SAT formula from a text file

    :file format:
    # comment
    A     # clause with unique positive literal
    :- A  # clause with unique negative literal
    A :- B, C, D # clause where A is positive and B,C,D negative
    # variables are strings without spaces
    """
    formula = []
    for line in open(filename, 'r'):
        line = line.strip()
        if line[0] == "#":
            continue
        lit = line.split(":-")
        if len(lit) == 1:
            posvar = lit[0]
            negvars = []
        else:
            assert len(lit) == 2
            posvar = lit[0].strip()
            if posvar == '':
                posvar = None
            negvars = lit[1].split(',')
            for i in range(len(negvars)):
                negvars[i] = negvars[i].strip()
        formula.append((posvar, negvars))
    return formula


def horn_sat(formula):
    """ Solving a HORN Sat formula

    :param formula: list of couple(posvar, negvars).
                    negvars is a list of the negative variables and can be empty.
                    posvar is the positive variable and can be None.
                    Variables can be any hashable objects, as integers or strings
                    for example.
    :returns: None if formula is not satisfiable, else a minimal set of variables
              that have to be set to true in order to satisfy the formula.
    :complexity: linear
    """
    # --- construct data structures
    CLAUSES = range(len(formula))
    score = [0 for c in CLAUSES]                # number of negative vars that are not yet in solution
    satisfied = [False for c in CLAUSES]
    posvar_in_clause = [None for c in CLAUSES]  # the unique positive variable of a clause (if any)
    clauses_with_posvar = defaultdict(set)      # all clauses where a variable appears positively
    clauses_with_negvar = defaultdict(set)      # all clauses where a variable appears negatively
    for c in CLAUSES:
        posvar, negvars = formula[c]
        score[c] = len(set(negvars))            # set data structure for clause c
        posvar_in_clause[c] = posvar
        if posvar is not None:
            clauses_with_posvar[posvar].add(c)
        for v in negvars:
            clauses_with_negvar[v].add(c)
        satisfied[c] = posvar in negvars
    pool = [set() for s in range(max(score) + 1)]   # create the pool
    for c in CLAUSES:
        pool[score[c]].add(c)                   # pool[s] = set of clauses with score s

    # --- solve Horn SAT formula
    solution = set()
    while pool[0]:
        curr = pool[0].pop()
        v = posvar_in_clause[curr]
        if v == None:
            return None   # formula is not satisfiable
        if v in solution or satisfied[curr]:
            continue                            # already processed v before
        solution.add(v)
        for c in clauses_with_negvar[v]:
            if c in pool[score[c]]:             # clause still active
                pool[score[c]].remove(c)
                score[c] -= 1
                assert score[c] >= 0
                pool[score[c]].add(c)               # change c to lower score in pool
        for c in clauses_with_posvar[v]:
            # c is now satisfied, we can ignore it from now on
            satisfied[c] = True
    return solution


if __name__=="__main__":
    F = _read(sys.argv[1])
    sol = horn_sat(F)
    if sol is None:
        print("No solution")
    else:
        print("Minimal solution:")
        for x in sorted(sol):
            print(x)
