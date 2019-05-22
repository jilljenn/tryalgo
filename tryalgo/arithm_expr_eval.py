#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Evaluate an arithmetic expression
jill-jenn vie et christoph durr - 2014-2018
-------------------------------------------

IPCELLS
http://www.spoj.com/problems/IPCELLS/
"""

from sys import stdin


# snip{ arithm_expr_eval
def arithm_expr_eval(cell_formula, expr):
    """Evaluates a given expression

    :param expr: expression
    :param cell_formula: dictionary variable name -> expression

    :returns: numerical value of expression

    :complexity: linear
    """
    if isinstance(expr, tuple):
        (left, operand, right) = expr
        lval = arithm_expr_eval(cell_formula, left)
        rval = arithm_expr_eval(cell_formula, right)
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
        cell_formula[expr] = arithm_expr_eval(cell_formula, cell_formula[expr])
        return cell_formula[expr]
# snip}


# snip{ arithm_expr_parse
PRIORITY = {';': 0, '(': 1, ')': 2, '-': 3, '+': 3, '*': 4, '/': 4}


def arithm_expr_parse(line_tokens):
    """Constructs an arithmetic expression tree

    :param line_tokens: list of token strings containing the expression
    :returns: expression tree

    :complexity:     line_tokensar
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


def _readint():
    return int(stdin.readline())


if __name__ == "__main__":
    # this main program is here to be tested on the online judge
    for test in range(_readint()):
        cell = {}
        stdin.readline()                     # consume the empty line
        for _ in range(_readint()):
            line = stdin.readline().split()
            cell[line[0]] = arithm_expr_parse(line[2:])
        for lhs in sorted(cell.keys()):
            print("%s = %i" % (lhs, arithm_expr_eval(cell, lhs)))
        print()
