#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Fast Fourier Transformation

christoph dürr - jill-jênn vie - 2022
"""
# http://www.cs.toronto.edu/~denisp/csc373/docs/tutorial3-adv-writeup.pdf
# https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm


import math     # for pi
import cmath    # for exp


def pad(x):
    """ pad array x with zeros to make its length a power of two
    :complexity: linear
    """
    n = 1
    while n < len(x):
        n <<= 1
    x += [0] * (n - len(x))


def fft(x):
    """ Fast Fourier Transformation
    :input x: list of coefficients. Length n has to be a power of 2.
    :returns: list of sample values.
    :complexity: O(n log n).
    """
    n2 = len(x) // 2
    if n2 == 0:
        return x
    assert(2 * n2 == len(x))        # need to split evenly
    even = fft(x[0::2])
    odd  = fft(x[1::2])
    T = [cmath.exp(-1j * math.pi * k / n2) * odd[k] for k in range(n2)]
    return [even[k] + T[k] for k in range(n2)] + \
           [even[k] - T[k] for k in range(n2)]


def inv_fft(y):
    """ Inverse Fast Fourier Transformation
    :input y: list of sample values. Length n has to be a power of 2.
    :returns: list of coefficients.
    :complexity: O(n log n).
    """
    n = len(y)
    p = fft([yi.conjugate() for yi in y])
    return [pi.conjugate() / n for pi in p]


def mul_poly_fft(p, q):
    """Multiply two polynomials in integer coefficient representation
    :complexity: O(n log n)
    """
    n = (len(p) + len(q))   # make them of same and enough large size
    p += [0] * (n - len(p))
    q += [0] * (n - len(q))
    pad(p)
    y = fft(p)
    pad(q)
    z = fft(q)
    n = len(y)  # the padding might have increased the size n
    r = [y[i] * z[i] for i in range(n)]
    R = inv_fft(r)
    return [int(round(ri.real)) for ri in R]
