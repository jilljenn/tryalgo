#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Huffman code

jill-jenn vie et christoph durr - 2014-2022
"""

from heapq import heappush, heappop


# snip{
def huffman(freq):
    """Huffman code

    :param freq: dictionary with frequencies for each item
    :returns: dictionary with binary code string for each item
    :complexity: O(n log n), where n = len(freq)
    """
    forest = []     # is a heap with (frequence, tree_index) pairs 
    trees = []      # list of trees, tree is a letter or a list of two trees
    for item in freq:
        heappush(forest, (freq[item], len(trees)))
        trees.append(item)  # this item will be at index len(trees)
    while len(forest) > 1:
        (f_l, left) = heappop(forest)        # merge two trees
        (f_r, right) = heappop(forest)
        heappush(forest, (f_l + f_r, len(trees)))
        trees.append([trees[left], trees[right]])
    code = {}                                # build code from unique tree
    extract(code, trees[forest[0][1]], [])
    return code


def extract(code, tree, prefix):
    """Extract Huffman code from a Huffman tree

    :param code: a dictionary that will contain the constructed code.
                 should initially be empty.
    :param tree: a node of the tree.
                 Leafs are of the form (frequency, symbol).
                 Inner nodes are of the form [left_sub_tree, right_sub_tree].
    :param prefix: a list with the 01 characters encoding the path from
                    the root to the node `tree`
    :complexity: O(n), where n = number of nodes in tree
    """
    if isinstance(tree, list):        # inner node
        left, right = tree
        prefix.append('0')
        extract(code, left, prefix)   # build code recursively
        prefix.pop()
        prefix.append('1')
        extract(code, right, prefix)  # ... on both subtrees
        prefix.pop()
    else:
        code[tree] = ''.join(prefix)  # extract codeword from prefix
# snip}
