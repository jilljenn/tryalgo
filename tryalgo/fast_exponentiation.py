#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Fast Exponentiation

jill-jenn vie et christoph durr and louis abraham - 2014-2018
"""


def fast_exponentiation2(a, b, q):
    """Compute (a pow b) % q

    :param int a b: non negative
    :param int q: positive
    :complexity: O(log b)
    """
    assert a >= 0 and b >= 0 and q >= 1
    p = 0               # only for documentation
    p2 = 1              # 2 ** p
    ap2 = a % q         # a ** (2 ** p)
    result = 1
    while b > 0:
        if p2 & b > 0:  # b's binary decomposition contains 2 ** p
            b -= p2
            result = (result * ap2) % q
        p += 1
        p2 *= 2
        ap2 = (ap2 * ap2) % q
    return result


# icpc-ignore
# snip{
def fast_exponentiation(a, b, q):
    """Compute (a pow b) % q, alternative shorter implementation

    :param int a b: non negative
    :param int q: positive
    :complexity: O(log b)
    """
    assert a >= 0 and b >= 0 and q >= 1
    result = 1
    while b:
        if b % 2 == 1:
            result = (result * a) % q
        a = (a * a) % q
        b >>= 1
    return result
# snip}

# snip{
def matrix_mul(A, B, q):
    """ multiples matrix A with B modulo q

    :param A, B: n by n matrix
    :complexity: O(n^3)
    """
    dim = range(len(A))
    AB = [[0 for j in dim] for i in dim]
    for i in dim:
        for j in dim:
            for k in dim:
                AB[i][j] = (AB[i][j] + A[i][k] * B[k][j]) % q 
    return AB


def matrix_fast_exponentiation(A, b, q):
    """Compute (A pow b) % q

    :param A: n by n matrix
    :param int b, q: positive integer
    :complexity: O(n^3 log b)
    """
    dim = range(len(A))
    result = [[int(i == j) for j in dim] for i in dim]
    while b:
        if b % 2 == 1:
            result = matrix_mul(result, A, q)
        A = matrix_mul(A, A, q)
        b >>= 1
    return result
# snip}
