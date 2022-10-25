#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Find substrings by Rabin-Karp

jill-jenn vie et christoph durr - 2015-2019
"""

# http://www.wolframalpha.com/input/?i=nearest+prime+number+to+2**56
# snip{ rabin_karp_roll_hash
PRIME = 72057594037927931     # < 2^{56}
DOMAIN = 128


def roll_hash(old_val, out_digit, in_digit, last_pos):
    """roll_hash """
    val = (old_val - out_digit * last_pos + DOMAIN * PRIME) % PRIME
    val = (val * DOMAIN) % PRIME
    return (val + in_digit) % PRIME
# snip}


# snip{ rabin_karp_matches
def matches(s, t, i, j, k):
    """
    Checks whether s[i:i + k] is equal to t[j:j + k].
    We used a loop to ease the implementation in other languages.
    """
    # tests if s[i:i + k] equals t[j:j + k]
    for d in range(k):
        if s[i + d] != t[j + d]:
            return False
    return True
# snip}


# snip{ rabin_karp_matching
def rabin_karp_matching(s, t):
    """Find a substring by Rabin-Karp

    :param s: the haystack string
    :param t: the needle string

    :returns: index i such that s[i: i + len(t)] == t, or -1
    :complexity: O(len(s) + len(t)) in expected time,
                and O(len(s) * len(t)) in worst case
    """
    hash_s = 0
    hash_t = 0
    len_s = len(s)
    len_t = len(t)
    last_pos = pow(DOMAIN, len_t - 1) % PRIME
    if len_s < len_t:              # substring too long
        return -1
    for i in range(len_t):         # preprocessing
        hash_s = (DOMAIN * hash_s + ord(s[i])) % PRIME
        hash_t = (DOMAIN * hash_t + ord(t[i])) % PRIME
    for i in range(len_s - len_t + 1):
        if hash_s == hash_t:                # hashes match
            # check character by character
            if matches(s, t, i, 0, len_t):
                return i
        if i < len_s - len_t:
            # shift window and calculate new hash on s
            hash_s = roll_hash(hash_s, ord(s[i]), ord(s[i + len_t]),
                               last_pos)
    return -1                               # no match
# snip}


# snip{ rabin_karp_factor
def rabin_karp_factor(s, t, k):
    """Find a common factor by Rabin-Karp

    :param string s: haystack
    :param string t: needle
    :param int k: factor length
    :returns: (i, j) such that s[i:i + k] == t[j:j + k] or None.
              In case of tie, lexicographical minimum (i, j) is returned
    :complexity: O(len(s) + len(t)) in expected time,
                and O(len(s) + len(t) * k) in worst case
    """
    last_pos = pow(DOMAIN, k - 1) % PRIME
    pos = {}
    assert k > 0
    if len(s) < k or len(t) < k:
        return None
    hash_t = 0

    # First calculate hash values of factors of t
    for j in range(k):
        hash_t = (DOMAIN * hash_t + ord(t[j])) % PRIME
    for j in range(len(t) - k + 1):
        # store the start position with the hash value
        if hash_t in pos:
            pos[hash_t].append(j)
        else:
            pos[hash_t] = [j]
        if j < len(t) - k:
            hash_t = roll_hash(hash_t, ord(t[j]), ord(t[j + k]), last_pos)

    hash_s = 0
    # Now check for matching factors in s
    for i in range(k):         # preprocessing
        hash_s = (DOMAIN * hash_s + ord(s[i])) % PRIME
    for i in range(len(s) - k + 1):
        if hash_s in pos:      # is this signature in s?
            for j in pos[hash_s]:
                if matches(s, t, i, j, k):
                    return (i, j)
        if i < len(s) - k:
            hash_s = roll_hash(hash_s, ord(s[i]), ord(s[i + k]), last_pos)
    return None
# snip}
