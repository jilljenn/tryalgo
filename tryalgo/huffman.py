#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Huffman code
jill-jenn vie et christoph durr - 2014-2018
"""

from heapq import heappush, heappop


# snip{
def huffman(freq=None):
    """Huffman code

    :param freq: dictionary with frequencies for each item
    :returns: dictionary with binary code string for each item
    :complexity: O(n log n)
    """
    h_u = []
    for item in freq:
        heappush(h_u, (freq[item], item))
    while len(h_u) > 1:
        (f_l, left) = heappop(h_u)
        (f_r, right) = heappop(h_u)
        heappush(h_u, (f_l + f_r, [left, right]))
    code = {}
    extract(code, h_u[0][1])
    return code


def extract(code=None, tree=None, prefix=[]):
    """Extract Huffman code from a Huffman tree

    :param tree: a node of the tree
    :param prefix: a list with the 01 characters encoding the path from
                    the root to the node `tree`
    :complexity: O(n)
    """
    if prefix is None:
        prefix = []
    if isinstance(tree, list):
        left, right = tree
        prefix.append('0')
        extract(code, left, prefix)
        prefix.pop()
        prefix.append('1')
        extract(code, right, prefix)
        prefix.pop()
    else:
        code[tree] = ''.join(prefix)
# snip}
