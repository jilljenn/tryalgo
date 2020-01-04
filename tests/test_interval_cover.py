# jill-jênn vie et christoph dürr - 2020
# coding=utf8

# pylint: disable=missing-docstring
import unittest
from tryalgo.interval_cover import _solve, interval_cover


class TestIntervalCover(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(_solve([(0, 0), (5, 0)], 3), 1)

    def test_interval_cover(self):
        L = [([(0, 1)], 1),
             ([(0, 3), (1, 2)], 1),
             ([(0, 2), (1, 3)], 1),
             ([(0, 2), (2, 3)], 1),
             ([(0, 2), (3, 4)], 2),
             ([(0, 4), (1, 3), (2, 6), (5, 8), (7, 9), (9, 10)], 3)]
        for instance, res in L:
            self.assertEqual(len(interval_cover(instance)), res)
