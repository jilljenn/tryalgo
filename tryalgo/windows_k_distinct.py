#!/usr/bin/env python3
# All sliding windows containing k distinct elements
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def windows_k_distinct(x, k):
    """Largest window containing k distinct elements

    :param x: list
    :yields: one largest interval [i, j] with this property
    :complexity: `O(|x|)`
    """
    i = 0
    j = 0
    nb_occ = {xi: 0 for xi in x}
    dist = 0                    # dist := nb z tel que nb_occ[z] > 0
    max_length = 0
    largest_pair = None
    while j < len(x) or (j == len(x) and dist >= k):
        if j < len(x) and (dist < k or (dist == k and nb_occ[x[j]] > 0)):
            if nb_occ[x[j]] == 0:
                dist += 1
            nb_occ[x[j]] += 1
            j += 1
        else:
            nb_occ[x[i]] -= 1
            if nb_occ[x[i]] == 0:
                dist -= 1
            i += 1
        if dist == k and j - i > max_length:
            max_length = j - i
            largest_pair = (i, j)
    return largest_pair
# snip}
