#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Huffman code
# jill-jenn vie et christoph durr - 2014-2018

from heapq import heappush, heappop


# snip{
def huffman(freq):
    """Huffman code

    :param freq: dictionary with frequencies for each item
    :returns: dictionary with binary code string for each item
    :complexity: O(n log n)
    """
    h = []
    for a in freq:
        heappush(h, (freq[a], a))
    while len(h) > 1:
        (fl, l) = heappop(h)
        (fr, r) = heappop(h)
        heappush(h, (fl + fr, [l, r]))
    code = {}
    extract(code, h[0][1])
    return code


def extract(code, tree, prefix=[]):
    """Extract Huffman code from a Huffman tree

    :param tree: a node of the tree
    :param prefix: a list with the 01 characters encoding the path from
                    the root to the node `tree`
    :complexity: O(n)
    """
    if isinstance(tree, list):
        l, r = tree
        prefix.append('0')
        extract(code, l, prefix)
        prefix.pop()
        prefix.append('1')
        extract(code, r, prefix)
        prefix.pop()
    else:
        code[tree] = ''.join(prefix)
# snip}
