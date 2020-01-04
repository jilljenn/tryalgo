# coding: utf8
# jill-jênn vie et christoph dürr - 2020

# pylint: disable=missing-docstring
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
from tryalgo.our_std import readint, readstr, readmatrix, readarray


class TestOurStd(unittest.TestCase):

    def test_readint(self):
        with patch('sys.stdin.readline', return_value="1"):
            self.assertEqual(readint(), 1)

    def test_readstr(self):
        with patch('sys.stdin.readline', return_value="  1 2 "):
            self.assertEqual(readstr(), "1 2")

    def test_readarray(self):
        with patch('sys.stdin.readline', return_value="1 2 3"):
            self.assertEqual(readarray(int), [1, 2, 3])

    def test_readmatrix(self):
        with patch('sys.stdin.readline', return_value="1 2 3"):
            self.assertEqual(readmatrix(3), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
