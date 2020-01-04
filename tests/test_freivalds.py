# coding: utf8
# jill-jênn vie et christoph dürr - 2020

# pylint: disable=missing-docstring
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
from tryalgo.freivalds import freivalds, readint, readmatrix, readarray


class TestNextPermutation(unittest.TestCase):

    def test_freivalds(self):
        A = [[2, 3], [3, 4]]
        B = [[1, 0], [1, 2]]
        C = [[5, 6], [7, 8]]
        self.assertTrue(freivalds(A, B, C))
        # [!] might fail with small probability

    def test_readint(self):
        with patch('sys.stdin.readline', return_value="1"):
            self.assertEqual(readint(), 1)

    def test_readarray(self):
        with patch('sys.stdin.readline', return_value="1 2 3"):
            self.assertEqual(readarray(int), [1, 2, 3])

    def test_readmatrix(self):
        with patch('sys.stdin.readline', return_value="1 2 3"):
            self.assertEqual(readmatrix(3), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
