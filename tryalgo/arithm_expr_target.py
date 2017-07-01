#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Create arithmetic expression approaching target value
# jill-jenn vie et christoph durr et jean-christophe filliatre - 2014-2017


# snip{
def arithm_expr_target(x, target):
    """ Create arithmetic expression approaching target value
    :param x: allowed constants
    :param target: target value
    :returns: string in form 'expression=value'
    :complexity: huge
    """
    n = len(x)
    expr = [{} for _ in range(1 << n)]  # expr[S][val] = string of expr. of value val using only values from set S
    for i in range(n):
        expr[1 << i] = {x[i]: str(x[i])}   # store singletons
    tout = (1 << n) - 1
    for S in range(3, tout + 1): # 3 = first number which is not a power of 2
        if expr[S] != {}:
            continue             # in that case S is a power of 2
        for L in range(1, S):    # decompose set S into non-empty sets L and R
            if L & S == L:
                R = S ^ L
                for vL in expr[L]:         # combine expressions from L
                    for vR in expr[R]:     # with expressions from R
                        eL = expr[L][vL]
                        eR = expr[R][vR]
                        expr[S][vL] = eL
                        if vL > vR:        # difference cannot become negative
                            expr[S][vL - vR] = "(%s-%s)" % (eL, eR)
                        if L < R:   # briser la symétrie
                            expr[S][vL + vR] = "(%s+%s)" % (eL, eR)
                            expr[S][vL * vR] = "(%s*%s)" % (eL, eR)
                        if vR != 0 and vL % vR == 0:  # only integer divisions
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

