# jill-jênn vie et christoph dürr - 2020
# coding=utf8

# pylint: disable=missing-docstring
import unittest
from tryalgo.next_permutation import next_permutation, solve_word_addition


class TestNextPermutation(unittest.TestCase):

    def test_solve_word_addition(self):
        self.assertEqual(solve_word_addition(["A", "B", "C"]), 32)
        self.assertEqual(solve_word_addition(["A", "B", "A"]), 0)

    def test_next_permutation(self):
        L = [2, 2, 0, 0, 1, 1, 0]
        self.assertEqual(next_permutation(L), True)
        self.assertEqual(L, [2, 2, 0, 1, 0, 0, 1])
        L = [2, 2, 1, 1, 0, 0, 0]
        self.assertEqual(next_permutation(L), False)
        L = [2]
        self.assertEqual(next_permutation(L), False)
        L = []
        self.assertEqual(next_permutation(L), False)
