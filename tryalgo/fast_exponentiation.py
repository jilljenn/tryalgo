#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fast Exponentiation
# jill-jenn vie et christoph durr and louis abraham - 2014-2018


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
        if b & 1:
            result = (result * a) % q
        a = ( a * a ) % q
        b >>= 1
    return result
# snip}
