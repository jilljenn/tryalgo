#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Create arithmetic expression approaching target value
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def all_subsets(n, card):
    """ generates all sets from {0, ..., n - 1} of cardinality card """
    if card == 0:
        yield 0
    else:
        for i in range(card - 1, n):
            for e in all_subsets(i, card - 1):
                yield e | (1 << i)


def arithm_expr_target(x, target):
    """ Create arithmetic expression approaching target value

    :param x: allowed constants
    :param target: target value
    :returns: string in form 'expression=value'
    :complexity: huge
    """
    n = len(x)
    expr = {}
    for i in range(n):
        expr[1 << i] = {x[i]: str(x[i])}
    tout = (1 << n) - 1
    for card in range(2, n + 1):
        for S in all_subsets(n, card):
            expr[S] = {}
            for L in range(1, S):
                if L & S == L:
                    R = S ^ L
                    for vL in expr[L]:
                        for vR in expr[R]:
                            eL = expr[L][vL]
                            eR = expr[R][vR]
                            expr[S][vL] = eL
                            expr[S][vL - vR] = "(%s-%s)" % (eL, eR)
                            if L < R:   # briser la symétrie
                                expr[S][vL + vR] = "(%s+%s)" % (eL, eR)
                                expr[S][vL * vR] = "(%s*%s)" % (eL, eR)
                            if vR != 0 and vL % vR == 0:
                                expr[S][vL // vR] = "(%s/%s)" % (eL, eR)
    # chercher expression la plus proche du but
    for dist in range(target + 1):
        for sign in [-1, +1]:
            val = target + sign * dist
            if val in expr[tout]:
                return "%s=%i" % (expr[tout][val], val)
    # partie jamais atteinte si x contient des nombres entre 0 et but
    pass
# snip}

