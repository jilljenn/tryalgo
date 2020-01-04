# coding: utf8
# jill-jênn vie et christoph dürr - 2020

# pylint: disable=missing-docstring
import unittest
from tryalgo.arithm import inv, pgcd, binom, binom_modulo


class TestArithm(unittest.TestCase):

    def test_inv(self):
        self.assertEqual(inv(8, 17), 15)

    def test_pgcd(self):
        self.assertEqual(pgcd(12, 18), 6)

    def test_binom(self):
        self.assertEqual(binom(4, 2), 6)

    def test_binom_modulo(self):
        self.assertEqual(binom_modulo(5, 2, 3), 1)
