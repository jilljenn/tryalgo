#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Evaluate an arithmetic expression

jill-jenn vie et christoph durr - 2014-2020
"""
# IPCELLS
# http://www.spoj.com/problems/IPCELLS/


from tryalgo.our_std import readint, readstr


# snip{ arithm_expr_eval
# pylint: disable=redefined-outer-name
# pylint: disable=inconsistent-return-statements
def arithm_expr_eval(cell, expr):
    """Evaluates a given expression

    :param expr: expression
    :param cell: dictionary variable name -> expression

    :returns: numerical value of expression

    :complexity: linear
    """
    if isinstance(expr, tuple):
        (left, operand, right) = expr
        lval = arithm_expr_eval(cell, left)
        rval = arithm_expr_eval(cell, right)
        if operand == '+':
            return lval + rval
        if operand == '-':
            return lval - rval
        if operand == '*':
            return lval * rval
        if operand == '/':
            return lval // rval
    elif isinstance(expr, int):
        return expr
    else:
        cell[expr] = arithm_expr_eval(cell, cell[expr])
        return cell[expr]
# snip}


# snip{ arithm_expr_parse
PRIORITY = {';': 0, '(': 1, ')': 2, '-': 3, '+': 3, '*': 4, '/': 4}


# pylint: disable=redefined-outer-name
def arithm_expr_parse(line_tokens):
    """Constructs an arithmetic expression tree

    :param line_tokens: list of token strings containing the expression
    :returns: expression tree

    :complexity: linear
    """
    vals = []
    ops = []
    for tok in line_tokens + [';']:
        if tok in PRIORITY:  # tok is an operator
            while (tok != '(' and ops and
                   PRIORITY[ops[-1]] >= PRIORITY[tok]):
                right = vals.pop()
                left = vals.pop()
                vals.append((left, ops.pop(), right))
            if tok == ')':
                ops.pop()    # this is the corresponding '('
            else:
                ops.append(tok)
        elif tok.isdigit():  # tok is an integer
            vals.append(int(tok))
        else:                # tok is an identifier
            vals.append(tok)
    return vals.pop()
# snip}


if __name__ == "__main__":
    # this main program is here to be tested on the online judge
    for test in range(readint()):
        cell = {}
        readstr()                     # consume the empty line
        for _ in range(readint()):
            line = readstr()
            cell[line[0]] = arithm_expr_parse(line[2:])
        for lhs in sorted(cell.keys()):
            print("%s = %i" % (lhs, arithm_expr_eval(cell, lhs)))
        print()
