"""  Rami Benelmir, Christoph Dürr, Erisa Kohansal - 2023

To verify which code lines are govered by the tests, execute

     coverage run -m unittest PC &&  coverage html

then open the file htmlcov/index.html.
"""

import unittest
from tryalgo.PC_tree import *

class Test_PC_tree(unittest.TestCase):

    def init_assertTrue(self):
        self.L = []

    def is_consecutive(self, order, R):
        n = len(order)
        B = [x in R for x in order]
        count = 0
        for i in range(n):
            if B[i] != B[i - 1]:
                count += 1
        return count == 2 

    def my_assertTrue(self, tmp, R):
        self.assertTrue(tmp.restrict(R))
        self.L.append(R)
        order = tmp.frontier()
        for R in self.L:
            self.assertTrue(self.is_consecutive(order, R))

    def my_assertFalse(self, tmp, R):
        self.assertFalse(tmp.restrict(R))
        order = tmp.frontier()
        self.assertFalse(self.is_consecutive(order, R))

    def test_OK(self):
        # we don't allow less than 3 leafs, by the invariant that every inner node has degree at least 3
        
        # Minus one
        tmp = T_prime = PC_tree(10)
        self.init_assertTrue()
        self.my_assertTrue(tmp, {1, 2, 3, 4, 5, 6, 7, 8})
        self.assertEqual(tmp, T_prime)

        # One permutation
        tmp = PC_tree(10)
        self.init_assertTrue()
        for i in range(9):
            self.my_assertTrue(tmp, {i, (i+1) % 10 })
        self.assertEqual(tmp.represent(), [['C', 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]])

    def test_represent(self):
        tmp = PC_tree(4)
        self.assertEqual(tmp.represent(True), [['P', 4, [0,1,2,3], None]])

    def test_TerminalPathNotSplittable(self):
        tmp = PC_tree(9)
        self.init_assertTrue()
        self.my_assertTrue(tmp, {3, 7})
        self.assertEqual(tmp.represent(), [['P', 9, [0, 1, 2, 4, 5, 6, 8, 10]], ['P', 10, [3, 7, 9]]])
        self.my_assertTrue(tmp, {1, 7})
        self.assertEqual(tmp.represent(), [['P', 9, [0, 2, 4, 5, 6, 8, 10]], ['C', 10, [1, 7, 3, 9]]])
        self.my_assertTrue(tmp, {1})
        self.assertEqual(tmp.represent(), [['P', 9, [0, 2, 4, 5, 6, 8, 10]], ['C', 10, [1, 7, 3, 9]]])
        self.my_assertFalse(tmp, {5, 7})
    
        tmp = PC_tree(20)
        self.assertTrue(tmp.restrict({3, 11, 13, 15, 19}))
        self.assertEqual(tmp.represent(), [['P', 20, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 17, 18, 21]], ['P', 21, [3, 11, 13, 15, 19, 20]]])
        self.assertTrue(tmp.restrict({11, 13, 15, 17, 19}))
        self.assertEqual(tmp.represent(), [['P', 20, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 21]], ['C', 21, [3, 20, 17, 22]], ['P', 22, [11, 13, 15, 19, 21]]])
        self.assertTrue(tmp.restrict({17, 19}))
        self.assertEqual(tmp.represent(), [['P', 20, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 21]], ['C', 21, [3, 20, 17, 19, 22]], ['P', 22, [11, 13, 15, 21]]])
        self.assertTrue(tmp.restrict({3, 13, 15}))
        self.assertEqual(tmp.represent(), [['P', 20, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 21]], ['C', 21, [3, 20, 17, 19, 11, 22]], ['P', 22, [13, 15, 21]]])
        
        tmp = PC_tree(5)
        self.assertTrue(tmp.restrict({0,1,2}))
        self.assertEqual(tmp.represent(), [['P', 5, [0, 1, 2, 6]], ['P', 6, [3, 4, 5]]])
        self.assertTrue(tmp.restrict({3,2}))
        self.assertEqual(tmp.represent(), [['P', 5, [0, 1, 6]], ['C', 6, [2, 3, 4, 5]]])
        self.assertFalse(tmp.restrict({1,3}))

        tmp = PC_tree(5)
        self.assertTrue(tmp.restrict({0,1,2}))
        self.assertEqual(tmp.represent(), [['P', 5, [0, 1, 2, 6]], ['P', 6, [3, 4, 5]]])
        self.assertTrue(tmp.restrict({2, 3}))
        self.assertEqual(tmp.represent(),[['P', 5, [0, 1, 6]], ['C', 6, [2, 3, 4, 5]]])
        self.assertFalse(tmp.restrict({1,3}))


    def test_Degree3Node(self):
        # PARTIAL

        tmp = PC_tree(20)
        self.assertTrue(tmp.restrict({9, 17}))
        self.assertEqual(tmp.represent(), [['P', 20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21]], ['P', 21, [9, 17, 20]]])
        self.assertTrue(tmp.restrict({1, 19, 17, 7}))
        self.assertEqual(tmp.represent(),  [['P', 20, [0, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18, 22]], ['P', 21, [1, 7, 19, 22]], ['C', 22, [9, 17, 21, 20]]])
        self.assertFalse(tmp.restrict({1, 7, 9, 13, 15}))

        tmp = PC_tree(8)
        self.assertTrue(tmp.restrict({1,3,5,6,7})) 
        self.assertEqual(tmp.represent(), [['P', 8, [0, 2, 4, 9]], ['P', 9, [1, 3, 5, 6, 7, 8]]])
        self.assertTrue(tmp.restrict({0,2,3,5,7}))
        self.assertEqual(tmp.represent(), [['P', 8, [0, 2, 11]], ['P', 9, [1, 6, 11]], ['P', 10, [3, 5, 7, 11]], ['C', 11, [4, 8, 10, 9]]])
        self.assertTrue(tmp.restrict({0,4}))
        self.assertEqual(tmp.represent(),  [['C', 8, [0, 2, 10, 9, 4]], ['P', 9, [1, 6, 8]], ['P', 10, [3, 5, 7, 8]]])
        self.assertTrue(tmp.restrict({3,5,7}))
        self.assertEqual(tmp.represent(),  [['C', 8, [0, 2, 10, 9, 4]], ['P', 9, [1, 6, 8]], ['P', 10, [3, 5, 7, 8]]])
        self.assertTrue(tmp.restrict({0,2}))
        self.assertEqual(tmp.represent(),  [['C', 8, [0, 2, 10, 9, 4]], ['P', 9, [1, 6, 8]], ['P', 10, [3, 5, 7, 8]]])
        self.assertFalse(tmp.restrict({0,2,3,6}))

        tmp = PC_tree(15)
        self.assertTrue(tmp.restrict({}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]])
        self.assertTrue(tmp.restrict({1,2,5,6}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 16]], ['P', 16, [1, 2, 5, 6, 15]]])
        self.assertTrue(tmp.restrict({7,8,9}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 3, 4, 10, 11, 12, 13, 14, 16, 17]], ['P', 16, [1, 2, 5, 6, 15]], ['P', 17, [7, 8, 9, 15]]])
        self.assertTrue(tmp.restrict({1,2,3,5,14}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 4, 10, 11, 12, 13, 18, 19]], ['P', 16, [1, 2, 5, 18]], ['P', 17, [3, 14, 18]], ['C', 18, [6, 15, 17, 16]], ['P', 19, [7, 8, 9, 15]]])
        self.assertFalse(tmp.restrict({5,6,7,10,14}))

        tmp = PC_tree(15)
        self.assertTrue(tmp.restrict({1,2,5,6}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 16]], ['P', 16, [1, 2, 5, 6, 15]]])
        self.assertTrue(tmp.restrict({7,8,9}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 3, 4, 10, 11, 12, 13, 14, 16, 17]], ['P', 16, [1, 2, 5, 6, 15]], ['P', 17, [7, 8, 9, 15]]])
        self.assertTrue(tmp.restrict({1,2,3,5,14}))
        self.assertEqual(tmp.represent(), [['P', 15, [0, 4, 10, 11, 12, 13, 18, 19]], ['P', 16, [1, 2, 5, 18]], ['P', 17, [3, 14, 18]], ['C', 18, [6, 15, 17, 16]], ['P', 19, [7, 8, 9, 15]]])
        self.assertFalse(tmp.restrict({5,6,7,10,14}))

        tmp = PC_tree(25)
        self.assertTrue(tmp.restrict({2,3,6,11,14,16,18}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 1, 4, 5, 7, 8, 9, 10, 12, 13, 15, 17, 19, 20, 21, 22, 23, 24, 26]], ['P', 26, [2, 3, 6, 11, 14, 16, 18, 25]]])
        self.assertTrue(tmp.restrict({0,1,3,8,9,10,12,16,17,21,22,23,24}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 1, 8, 9, 10, 12, 17, 21, 22, 23, 24, 29]], ['P', 26, [2, 6, 11, 14, 18, 29]], ['P', 27, [3, 16, 29]], ['P', 28, [4, 5, 7, 13, 15, 19, 20, 29]], ['C', 29, [25, 27, 26, 28]]])
        self.assertFalse(tmp.restrict({0,4,5,6,8,12,13,14,21}))

        tmp = PC_tree(25)
        self.assertTrue(tmp.restrict({0,2,3,4,5,7,8,11,12,16,17,18,20,21,22}))
        self.assertTrue(tmp.restrict({1,2,6,7,10,13,17,21,22}))
        self.assertFalse(tmp.restrict({0,2,3,4,8,11,12,13,14,15,17,19,21,24}))

        tmp = PC_tree(25)
        self.assertTrue(tmp.restrict({0,1,3,4,5,7,8,9,10,11,12,14,15,16,17,18,19,20,22,24}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26]], ['P', 26, [2, 6, 13, 21, 23, 25]]])
        self.assertTrue(tmp.restrict({0,1,2,4,8,9,10,11,15,16,17,19,22,23}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 1, 4, 8, 9, 10, 11, 15, 16, 17, 19, 22, 29]], ['P', 26, [2, 23, 29]], ['P', 27, [3, 5, 7, 12, 14, 18, 20, 24, 29]], ['P', 28, [6, 13, 21, 29]], ['C', 29, [25, 26, 28, 27]]])
        self.assertFalse(tmp.restrict({4,6,7,9,11,15,16,20}))

        tmp = PC_tree(25)
        self.assertTrue(tmp.restrict({0,1,2,3,5,7,11,15,19,23,24}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 1, 2, 3, 5, 7, 11, 15, 19, 23, 24, 26]], ['P', 26, [4, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 25]]])
        self.assertTrue(tmp.restrict({0,2,4,5,6,7,10,11,12,13,14,15,18,20,21,22}))
        self.assertEqual(tmp.represent(), [['P', 25, [0, 2, 5, 7, 11, 15, 29]], ['P', 26, [1, 3, 19, 23, 24, 29]], ['P', 27, [4, 6, 10, 12, 13, 14, 18, 20, 21, 22, 29]], ['P', 28, [8, 9, 16, 17, 29]], ['C', 29, [25, 26, 28, 27]]])
        self.assertFalse(tmp.restrict({2,6,7,12,13,14,15,16,17,18,20,21,24}))

        # WITHOUT PARTIAL
        tmp = PC_tree(10)
        self.assertTrue(tmp.restrict({0,1}))
        self.assertEqual(tmp.represent(), [['P', 10, [0, 1, 11]], ['P', 11, [2, 3, 4, 5, 6, 7, 8, 9, 10]]])
        self.assertTrue(tmp.restrict({2,3,4,5}))
        self.assertEqual(tmp.represent(),[['P', 10, [0, 1, 12]], ['P', 11, [2, 3, 4, 5, 12]], ['P', 12, [6, 7, 8, 9, 10, 11]]])
        self.assertTrue(tmp.restrict({0,1,2,3,6,7}))
        self.assertEqual(tmp.represent(),[['P', 10, [0, 1, 13]], ['P', 11, [2, 3, 15]], ['P', 12, [4, 5, 15]], ['P', 13, [6, 7, 10, 15]], ['P', 14, [8, 9, 15]], ['C', 15, [11, 12, 14, 13]]])
        self.assertTrue(tmp.restrict({3,4}))
        self.assertEqual(tmp.represent(), [['P', 10, [0, 1, 12]], ['C', 11, [2, 3, 4, 5, 13, 12]], ['P', 12, [6, 7, 10, 11]], ['P', 13, [8, 9, 11]]])
        
    def test_UniqueCNode(self):
        tmp = PC_tree(9)
        self.assertTrue(tmp.restrict({0,1}))
        self.assertEqual(tmp.represent(), [['P', 9, [0, 1, 10]], ['P', 10, [2, 3, 4, 5, 6, 7, 8, 9]]])
        self.assertTrue(tmp.restrict({0,2}))
        self.assertEqual(tmp.represent(), [['C', 9, [0, 1, 10, 2]], ['P', 10, [3, 4, 5, 6, 7, 8, 9]]])
        self.assertFalse(tmp.restrict({1,2}))

        tmp = PC_tree(10)
        self.assertTrue(tmp.restrict({1,2}))
        self.assertTrue(tmp.restrict({3,2}))
        self.assertTrue(tmp.restrict({0,4}))
        self.assertTrue(tmp.restrict({0,5}))
        self.assertEqual(tmp.represent(), [['C', 10, [0, 4, 12, 5]], ['C', 11, [1, 2, 3, 12]], ['P', 12, [6, 7, 8, 9, 10, 11]]])

        tmp = PC_tree(10)
        self.assertTrue(tmp.restrict({1,4,6,7}))
        self.assertTrue(tmp.restrict({1,4,6,7,8,9}))
        self.assertFalse(tmp.restrict({1,2,5,6,9}))
        self.assertFalse(tmp.restrict({0,1,3,4,5,6,8}))
        self.assertTrue(tmp.restrict({0,1,2,4,7}))
        self.assertEqual(tmp.represent(),  [['P', 10, [0, 2, 13]], ['P', 11, [1, 4, 7, 13]], ['P', 12, [3, 5, 13]], ['C', 13, [6, 11, 10, 12, 14]], ['P', 14, [8, 9, 13]]])
        self.assertFalse(tmp.restrict({0,1,2,3,4,5,6}))
        self.assertTrue(tmp.restrict({0,1,2,3,4,5,6,7}))
        self.assertFalse(tmp.restrict({2,4,6}))
        self.assertFalse(tmp.restrict({2,3,4,5,6,7,9}))
        self.assertFalse(tmp.restrict({1,2,6,8}))
    
    def test_80(self):
        # this generates a spider graph with 4 legs
        tmp = PC_tree(80)
        for d in range(0, 80, 20):
            for i in range(0, 20, 2):
                tmp.restrict(range(d + i, d + 20 - i))
        tmp.restrict({6, 7, 8})
        tmp.restrict({4,6,7})
        tmp.restrict({5, 6})
        tmp.restrict({10, 12})
        tmp.restrict([7, 5, 8, 6])
        tmp.restrict([5, 7, 8, 6])
        tmp.restrict({20, 40, 60})
        tmp.restrict({31, 28})
        tmp.restrict({32, 33})
        # rep2dot(tmp.represent(True))
        tmp.restrict({22, 27})

    def test_Fink_Pfretzschner_Rutter_Appendix_B1(self):
        tmp = PC_tree(6)
        tmp.restrict({1, 2})
        tmp.restrict({2, 3})
        tmp.restrict({4, 5})
        tmp.restrict({5, 0})
        self.assertEqual(tmp.represent(False), [['C', 6, [0, 5, 4, 7]], ['C', 7, [1, 2, 3, 6]]])

if __name__ == '__main__':
    unittest.main()