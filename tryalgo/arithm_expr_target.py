#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Create arithmetic expression approaching target value
# jill-jenn vie et christoph durr et jean-christophe filliatre - 2014-2018


# snip{
def arithm_expr_target(x, target):
    """ Create arithmetic expression approaching target value
    :param x: allowed constants
    :param target: target value
    :returns: string in form 'expression=value'
    :complexity: huge
    """
    n = len(x)
    expr = [{} for _ in range(1 << n)]
    # expr[S][val]
    # = string solely composed of values in set S that evaluates to val
    for i in range(n):
        expr[1 << i] = {x[i]: str(x[i])}   # store singletons
    all_ = (1 << n) - 1
    for S in range(3, all_ + 1): # 3: first number that isn't a power of 2
        if expr[S] != {}:
            continue            # in that case S is a power of 2
        for L in range(1, S):   # decompose set S into non-empty sets L, R
            if L & S == L:
                R = S ^ L
                for vL in expr[L]:         # combine expressions from L
                    for vR in expr[R]:     # with expressions from R
                        eL = expr[L][vL]
                        eR = expr[R][vR]
                        expr[S][vL] = eL
                        if vL > vR:    # difference cannot become negative
                            expr[S][vL - vR] = "(%s-%s)" % (eL, eR)
                        if L < R:      # break symmetry
                            expr[S][vL + vR] = "(%s+%s)" % (eL, eR)
                            expr[S][vL * vR] = "(%s*%s)" % (eL, eR)
                        if vR != 0 and vL % vR == 0:  # only integer div
                            expr[S][vL // vR] = "(%s/%s)" % (eL, eR)
    # look for the closest expression from the target
    for dist in range(target + 1):
        for sign in [-1, +1]:
            val = target + sign * dist
            if val in expr[all_]:
                return "%s=%i" % (expr[all_][val], val)
    # never reaches here if x contains integers between 0 and target
    pass
# snip}
