#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Solving Horn SAT

# christoph dürr - 2016-2018


"""
clauses are numbered starting from 0
variables are strings (identifier)

solution  : set of variables that are set to true
posvar_in_clause : maps clause to the unique positive variable in clause (or None)
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
    posvar_in_clause = [None for c in CLAUSES]  # the unique positive variable of a clause (if any)
    clauses_with_negvar = defaultdict(set)      # all clauses where a variable appears negatively
    for c in CLAUSES:
        posvar, negvars = formula[c]
        score[c] = len(set(negvars))            # do not count twice repeated negative variables
        posvar_in_clause[c] = posvar
        for v in negvars:
            clauses_with_negvar[v].add(c)
    pool = [set() for s in range(max(score) + 1)]   # create the pool
    for c in CLAUSES:
        pool[score[c]].add(c)                   # pool[s] = set of clauses with score s

    # --- solve Horn SAT formula
    solution = set()                            # contains all variables set to True
    while pool[0]:
        curr = pool[0].pop()                    # arbitrary zero score clause
        v = posvar_in_clause[curr]
        if v == None:                           # formula is not satisfiable
            return None
        if v in solution or curr in clauses_with_negvar[v]:
            continue                            # clause is already satisfied
        solution.add(v)
        for c in clauses_with_negvar[v]:        # update score
            pool[score[c]].remove(c)
            score[c] -= 1
            pool[score[c]].add(c)               # change c to lower score in pool
    return solution


if __name__=="__main__":
    F = read(sys.argv[1])
    sol = horn_sat(F)
    if sol is None:
        print("No solution")
    else:
        print("Minimal solution:")
        for x in sorted(sol):
            print(x)
