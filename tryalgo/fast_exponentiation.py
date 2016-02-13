#!/usr/bin/env python3
# Fast Exponentiation
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def fast_exponentiation(a, b, q):
    """Compute (a pow b) % q
    :complexity: O(log b)
    """
    assert a >= 0 and b >= 0 and q >= 1
    result = 1
    while b:
        if b & 1:
            result = (result * a) % q
        a = a * a % q
        b >>= 1
    return result
# snip}

